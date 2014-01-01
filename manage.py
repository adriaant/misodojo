#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

if __name__ == "__main__":
    environment = os.environ.get('PROJECT_ENV', 'dev')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "misodojo.settings.%s" % environment)
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
