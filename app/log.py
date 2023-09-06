import logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'root_formatter': {
            'format': '%(asctime)s %(req_id)s %(message)s',
        },
    },
    'filters': {
        'root_filter': {
            '()': 'log_utils.RootFilter',
        },
        'requests_filter': {
          '()': 'log_utils.RequestsFilter'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'root_formatter',
        },
        'requests_file_handler': {
            'level': logging.INFO,
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': 'logs/requests.log',
            'when': 'midnight',
            'backupCount': 0,
            'formatter': 'root_formatter'
        },
    },
    'loggers': {
        'root': {
            'level': logging.INFO,
            'handlers': ['console'],
            'propagate': False,
        },
        'requests': {
            'level': logging.INFO,
            'handlers': ['requests_file_handler'],
            'filters': ['requests_filter'],
            'propagate': True,
            'formatters': ['requests_formatter']
        }
    }
}
