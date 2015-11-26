"""
Common code used to streamline testing.

pytest documentation: http://pytest.org/latest/contents.html
"""
from __future__ import absolute_import, print_function

import os
import shutil

STAGING = '/tmp/staging'


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
