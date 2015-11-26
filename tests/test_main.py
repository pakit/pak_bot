"""
Test pak_bot.main
"""
from __future__ import absolute_import, print_function

import pak_bot.main


def test_main(mock_print):
    pak_bot.main.main()
    mock_print.assert_any_call('hello')
