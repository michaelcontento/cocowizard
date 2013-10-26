# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sys
import os
import traceback
from colorama import Fore, Back, Style

def error(message, exit=True, end="\n"):
    print(Fore.RED + "[ERROR]", message, Style.RESET_ALL, end=end)
    if exit:
        sys.exit()

def warning(message, end="\n"):
    print(Fore.YELLOW + "[WARN]", message, Style.RESET_ALL, end=end)

def info(message, end="\n"):
    print("[INFO]", message, end=end)

def debug(message, end="\n"):
    if "DEBUG" not in os.environ:
        return

    if isinstance(message, BaseException):
        print(Back.RED + Fore.BLACK + "[EXCEPTION]", message, Style.RESET_ALL)
        traceback.print_exc()
    else:
        print(Fore.GREEN + "[DEBUG]", message, Style.RESET_ALL, end=end)
