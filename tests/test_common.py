"""
Test tests.common
"""
from __future__ import absolute_import
import mock
import os

import tests.common as tc


def test_env_setup():
    assert os.path.exists(tc.RECIPES)


@mock.patch('tests.common.shutil')
def test_env_teardown(mock_shutil):
    tc.env_teardown()
    mock_shutil.rmtree.assert_any_call(tc.RECIPES)
