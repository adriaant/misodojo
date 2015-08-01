# -*- coding: utf-8 -*-
"""
Settings for local development.
"""
import os

# Import base settings
from .base import *  # pylint: disable=W0614,W0401


# ==============================================================================
# Generic Django project settings
# ==============================================================================

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Output to use in template system for invalid (e.g. misspelled) variables.
TEMPLATE_STRING_IF_INVALID = "!! INVALID '%s' !!"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'miso',
        'USER': 'miso',
        'PASSWORD': 'linuxcare',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': 300,
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    }
}

# ==============================================================================
# WSGI
# ==============================================================================

WSGI_APPLICATION = "misodojo.wsgi.dev.application"

# ==============================================================================
# Email backend
# ==============================================================================

# Discard all emails sent.
EMAIL_BACKEND = "django.core.mail.backends.dummy.EmailBackend"

# ==============================================================================
# Debugging
# ==============================================================================
# app: debug_toolbar

INSTALLED_APPS += ("debug_toolbar",)
MIDDLEWARE_CLASSES += ("debug_toolbar.middleware.DebugToolbarMiddleware",)
INTERNAL_IPS = ("127.0.0.1",)
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]
DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
    # "SHOW_TOOLBAR_CALLBACK": custom_show_toolbar,
    # "EXTRA_SIGNALS": ["project.signals.MySignal"],
    # "HIDE_DJANGO_SQL": True,
    # "SHOW_TEMPLATE_CONTEXT": True,
    # "TAG": "body",
}

# ==============================================================================
# Haystack configuration
# ==============================================================================

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.realpath(os.path.join(VAR_ROOT, "whoosh_index"))
    },
}

# ==============================================================================
# Logging
# ==============================================================================

# See http://docs.djangoproject.com/en/dev/topics/logging for more details.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'log_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/tmp/django.log',
            'maxBytes': '16777216',  # 16megabytes
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['log_file'],
            'level': 'ERROR',
            'propagate': True,
        },
        'apps': {
            'handlers': ['log_file'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}

# ==============================================================================
# My personal settings
# ==============================================================================

try:
    from .mine import *  # pylint: disable=W0614,W0401
except:
    pass
