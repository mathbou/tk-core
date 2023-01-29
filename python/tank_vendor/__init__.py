# Copyright (c) 2016 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

# FIXME most of Tk frameworks need tank_vendor namespace for their imports => /!\ REALLY BAD DESIGN, THEY SHOULD NOT RELIES ON CORE VENDOR /!\

__all__ = ["six", "distro", "shotgun_authentication", "shotgun_api3", "ruamel_yaml", "yaml"]

import six
import distro
import shotgun_api3
import yaml

try:
    import ruamel.yaml as ruamel_yaml
except ImportError:
    import ruamel_yaml

from . import shotgun_authentication
