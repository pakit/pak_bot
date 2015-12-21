"""
Example of what test file should look like generated.
"""
from __future__ import absolute_import, print_function
import os
import shutil
import pytest

import pakit.conf
import pakit.main
import pakit.recipe
import pakit.task


def delete_it(path):
    """
    File or folder, it is deleted.

    Args:
        path: path to a file or dir
    """
    try:
        shutil.rmtree(path)
    except OSError:
        try:
            os.remove(path)
        except OSError:
            pass


@pytest.fixture(scope='session', autouse=True)
def setup_test_bed(request):
    """
    Fixture sets up the testing environment for pakit as a whole.

    Session scope, executes before all tests.
    """
    def env_teardown():
        """
        Cleanup post test run.
        """
        delete_it(os.path.dirname(pakit.conf.CONFIG.path_to('link')))

    request.addfinalizer(env_teardown)

    root = os.getcwd()
    while not os.path.exists(os.path.join(root, '.travis.yml')):
        root = os.path.dirname(root)

    args = pakit.main.create_args_parser().parse_args(['available'])
    args.conf = os.path.join(root, 'tests', 'pakit.yml')
    pakit.main.global_init(args.conf)


class BaseRecipeTest(object):
    def setup(self):
        name = self.__class__.__name__.replace('Test_', '')
        self.recipe = pakit.recipe.RDB.get(name)

    def teardown(self):
        for leaf in ['prefix', 'source', 'link']:
            path = pakit.conf.CONFIG.path_to(leaf)
            delete_it(path)
            try:
                os.makedirs(path)
            except OSError:
                pass
        if self.recipe.name in pakit.conf.IDB:
            pakit.conf.IDB.remove(self.recipe.name)


class Test_ag(BaseRecipeTest):
    def test_stable(self):
        self.recipe.repo = 'stable'
        pakit.task.InstallTask(self.recipe).run()

    def test_unstable(self):
        self.recipe.repo = 'unstable'
        pakit.task.InstallTask(self.recipe).run()
