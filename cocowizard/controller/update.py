# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sh
from path import path

from ..utils import config
from ..utils.log import debug, indent
from .configure_icons import run as configure_icons
from .configure_dependencies import run as configure_dependencies
from .configure_projects import run as configure_projects
from .generate_icons import run as generate_icons
from .recreate_projects import run as recreate_projects
from .configure_package import run as configure_package
from .generate_screenshots import run as generate_screenshots

def run():
    steps = [
        recreate_projects,
        configure_dependencies,
        configure_projects,
        generate_icons,
        configure_icons,
        configure_package,
        generate_screenshots
    ]

    for step in steps:
        name = step.__module__.split(".")[-1]
        debug("Run controller: %s" % name)
        with indent():
            step()
