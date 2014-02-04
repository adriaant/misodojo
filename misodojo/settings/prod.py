# -*- coding: utf-8 -*-
"""
Settings for Production Server.
"""
# Import base settings.
from .base import *  # pylint: disable=W0614,W0401

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'miso',
        'USER': 'miso',
        'PASSWORD': PWD_MYSQL,
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

ALLOWED_HOSTS = ['.infinite-sushi.com']
MEDIA_ROOT = "/home/sushi/media"
STATIC_ROOT = "/home/sushi/static"

#==============================================================================
# Haystack configuration
#==============================================================================

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': "/home/sushi/data/whoosh_index"
    },
}

#==============================================================================
# Error & logging
#==============================================================================

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
            'level': 'INFO',
            'class': 'django.utils.log.NullHandler',
        },
        'log_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/home/sushi/logs/django.log',
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
            'level': 'INFO',
            'propagate': True,
        }
    }
}
