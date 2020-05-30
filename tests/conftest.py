# -*- coding: utf-8 -*-

"""
This module is used to provide configuration, fixtures, and plugins for pytest.

It may be also used for extending doctest's context:
1. https://docs.python.org/3/library/doctest.html
2. https://docs.pytest.org/en/latest/doctest.html
"""

import os

TEST_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
HTTP_SERVER_HOSTNAME = "127.0.0.1"
HTTP_SERVER_PORT = 65000

OAUTH_CODE = "anime_girls_are_cute"
