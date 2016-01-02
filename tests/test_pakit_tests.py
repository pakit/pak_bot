"""
Test pakit_tests
"""
from __future__ import absolute_import, print_function
import os
import tempfile
import mock
import pytest

from pakit_tests import (
    create_args_parser, extract_repo_names, extract_repo_block, main,
    scan_recipes, format_lines, write_file, TEMPLATE
)
import tests.common as tc


def test_parse_recipes_root():
    root = os.path.abspath('recipes')
    args = create_args_parser().parse_args([root])
    assert args.recipes_root == root
    assert args.output == os.path.join('tests', 'test_recipes.py')


def test_parse_output():
    root = os.path.abspath('recipes')
    argv = '{0} {1}'.format(root, 'test_recs.py').split()
    args = create_args_parser().parse_args(argv)
    assert args.recipes_root == root
    assert args.output == 'test_recs.py'


def test_extract_repo_names():
    text = """self.repos = {
    'stable': Git(self.src, tag='0.31.0'),
    'unstable': Git(self.src),
    }"""
    assert extract_repo_names(text) == ['stable', 'unstable']


def test_extract_repo_block():
    text = """class Ag(Recipe):
    \"\"\"
    Grep like tool optimized for speed
    \"\"\"
    def __init__(self):
        super(Ag, self).__init__()
        self.src = 'https://github.com/ggreer/the_silver_searcher.git'
        self.homepage = self.src
        self.repos = {
            "stable": Git(self.src, tag='0.31.0'),
            'unstable': Git(self.src),
        }

    def build(self):
        self.cmd('./build.sh --prefix {prefix}')
        self.cmd('make install')"""
    expect = """self.repos = {
            "stable": Git(self.src, tag='0.31.0'),
            'unstable': Git(self.src),
        }"""
    assert extract_repo_block(text) == expect


def test_scan_recipes():
    data = scan_recipes(tc.RECIPES)
    assert 'ag' in data
    assert sorted(data['ag']) == ['stable', 'unstable']


def test_format_lines():
    data = {
        'ag': ['stable', 'unstable'],
        'ack': ['stable'],
    }
    lines = format_lines(data)
    expect = """\nclass Test_ack(RecipeTest):
    def test_stable(self):
        assert subprocess.call(self.args, cwd=self.temp_d,
                               env=self.new_env) == 0

\nclass Test_ag(RecipeTest):
    def test_stable(self):
        assert subprocess.call(self.args, cwd=self.temp_d,
                               env=self.new_env) == 0

    def test_unstable(self):
        assert subprocess.call(self.args, cwd=self.temp_d,
                               env=self.new_env) == 0"""

    assert '\n'.join(lines) == expect


def test_write_file():
    try:
        test_file = tempfile.NamedTemporaryFile()
        write_file(tc.RECIPES, test_file.name)
        with open(test_file.name, 'r') as fin:
            assert TEMPLATE.replace('ROOT_RECS', tc.RECIPES) in fin.read()
    finally:
        test_file.close()


@mock.patch('pakit.main.argparse._sys')
def test_main_args_none(mock_sys):
    with pytest.raises(AttributeError):
        main(['pakit_tests'])
    mock_sys.exit.assert_called_with(2)


@mock.patch('pakit_tests.write_file')
def test_main_output_absolutel(mock_write, mock_print):
    main(['pakit_tests', '.', '/dev/null'])
    mock_print.assert_any_call('Scanning recipes under: ' + os.getcwd())
    mock_print.assert_any_call('Writing tests to: /dev/null')


@mock.patch('pakit_tests.write_file')
def test_main_output_relative(mock_write, mock_print):
    main(['pakit_tests', '/tmp'])
    mock_print.assert_any_call('Scanning recipes under: /tmp')
    mock_print.assert_any_call('Writing tests to: /tmp/tests/test_recipes.py')
    mock_write.assert_any_call('/tmp', '/tmp/tests/test_recipes.py')
