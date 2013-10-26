# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sh
from path import path

from ..cli import debug
from .recreate_projects import run as recreate_projects
from .configure_libraries import run as configure_libraries

def run():
    debug(">>> recreate_projects")
    recreate_projects()

    debug(">>> configure_libraries")
    configure_libraries()
