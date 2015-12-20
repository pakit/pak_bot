"""
Common code used to streamline testing.

pytest documentation: http://pytest.org/latest/contents.html
"""
from __future__ import absolute_import, print_function
import os
import shlex
import shutil
import subprocess as sub

STAGING = '/tmp/bot_staging'
RECIPES = os.path.join(STAGING, 'recipes')
RECIPES_URI = 'https://github.com/pakit/test_recipes'


def env_setup():
    """
    Setup for test run.
    """
    print('\n-----INIT ENV')
    cmd = 'git clone --depth 1 {0} {1}'.format(RECIPES_URI, RECIPES)
    sub.call(shlex.split(cmd))
    print('\n-----INIT ENV FINISHED')


def env_teardown():
    """
    Cleanup post test run.
    """
    delete_it(RECIPES)


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
