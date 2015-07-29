#!/usr/bin/env python

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'debug': {
            'format': '[%(levelname)s][%(asctime)s](%(funcName)s/%(lineno)d) %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {                                                                                                                           'format': '[%(levelname)s][%(asctime)s] %(message)s',                                                                              'datefmt': '%y %b %d, %H:%M:%S',
            'format': '[%(levelname)s][%(asctime)s] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'test.log',
            'formatter': 'simple',
            'maxBytes': 1024 * 1024 * 10,  # 10 mb
            'backupCount': 100
        },
    },
    'loggers': {
        'my_app': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False
        },
    }
}

from logging.config import dictConfig
dictConfig(LOGGING)
