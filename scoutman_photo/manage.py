#!/usr/bin/env python
import os
import sys
from common.utils import read_env

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scoutman_photo.settings.local")

    from django.core.management import execute_from_command_line
    read_env()
    execute_from_command_line(sys.argv)
