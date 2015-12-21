"""
Common code used to streamline testing.

pytest documentation: http://pytest.org/latest/contents.html
"""
from __future__ import absolute_import, print_function
import os
import shlex
import shutil
import subprocess as sub

STAGING = '/tmp/staging'
RECIPES = os.path.join(STAGING, 'recipes')
RECIPES_URL = 'https://github.com/pakit/base_recipes'


def env_setup():
    """
    Setup for test run.
    """
    cmd = shlex.split('git clone {0} {1}'.format(RECIPES_URL, RECIPES))
    sub.call(cmd)


def env_teardown():
    """
    Cleanup post test run.
    """
    delete_it(STAGING)


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
