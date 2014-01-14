# -*- coding: utf-8 -*-
"""
Base settings shared by all environments.
"""
import os
import sys

import misodojo as project_module

# Import global settings to make it easier to extend settings.
from django.conf.global_settings import *   # pylint: disable=W0614,W0401
from .secrets import *  # passwords and stuff, things you wouldn't put under source control

#==============================================================================
# Generic Django project settings
#==============================================================================

SITE_ID = 1

ADMINS = (
    ('Adriaan Tijsseling', 'adriaangt@gmail.com'),
)
MANAGERS = ADMINS

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'UTC'
USE_TZ = True
USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', 'English'),
)

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []


#==============================================================================
# Directories
#==============================================================================
# Best Practice: The suffix ``_ROOT`` is reserved for writable locations.

# Absolute filesystem path to the project module.
PROJECT_DIR = os.path.dirname(os.path.realpath(project_module.__file__))

# Absolute filesystem path to the main package.
PACKAGE_DIR = os.path.realpath(os.path.join(PROJECT_DIR, ".."))

# Absolute filesystem path to /var dirs.
VAR_ROOT = os.path.realpath(os.path.join(PACKAGE_DIR, "var"))
LOCALE_ROOT = os.path.realpath(os.path.join(VAR_ROOT, "locale"))
LOG_ROOT = os.path.realpath(os.path.join(VAR_ROOT, "log"))

# Tuple of directories where Django looks for translation files.
# Django will look within each of these paths for the
# <locale_code>/LC_MESSAGES directories containing the actual translation
# files.
LOCALE_PATHS = (LOCALE_ROOT,)

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/static.example.com/media/"
MEDIA_ROOT = os.path.realpath(os.path.join(VAR_ROOT, "media"))

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
STATIC_ROOT = os.path.realpath(os.path.join(VAR_ROOT, "static"))

# Additional locations (absolute paths) of static files.
# Always use Unix-style forward slashes, even on Windows.
STATICFILES_DIRS = (
    os.path.realpath(os.path.join(PROJECT_DIR, "static")),
)

# List of locations of the template source files, in search order.
# Always use Unix-style forward slashes, even on Windows.
TEMPLATE_DIRS = (
    os.path.realpath(os.path.join(PROJECT_DIR, "templates")),
)

# Optionally, create missing directories where files could be written.
#for d in (VAR_ROOT, LOCALE_ROOT, LOG_ROOT, MEDIA_ROOT, STATIC_ROOT):
#    if not os.path.exists(d):
#        os.mkdir(d)

# append the apps to the path so we can list app names under 'INSTALLED_APPS'
sys.path.append(os.path.join(PROJECT_DIR, 'apps'))

#==============================================================================
# Project URLS and media settings
#==============================================================================

# for Grappelli we need to explictly have the right order
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

ROOT_URLCONF = 'misodojo.urls'

# Base URL.
# Make sure to use a trailing slash, or "/" if no sub-path.
BASE_URL = "/"

# URL that handles the static files uploaded via the app served from MEDIA_ROOT.
# Make sure to use a trailing slash.
# Examples: "http://example.com/media/", "http://static.example.com/media/"
MEDIA_URL = BASE_URL + "media/"

# URL that handles the static files served from STATIC_ROOT.
# Examples: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = BASE_URL + "static/"

#==============================================================================
# Templates
#==============================================================================

TEMPLATE_CONTEXT_PROCESSORS += (
    "django.core.context_processors.request",  # for Grappelli
)

#==============================================================================
# Middleware
#==============================================================================

MIDDLEWARE_CLASSES += (
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

#==============================================================================
# Apps
#==============================================================================

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'grappelli',
    'django.contrib.admin',
    'crispy_forms',  # Form layouts
    'south',
    'taggit',
    'blog',
    'core',
)

#==============================================================================
# Miscellaneous project settings
#==============================================================================

#==============================================================================
# Third party app settings
#==============================================================================

CRISPY_TEMPLATE_PACK = 'bootstrap3'
AUTOSLUG_SLUGIFY_FUNCTION = "slugify.slugify"
