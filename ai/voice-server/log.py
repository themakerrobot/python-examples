import logging
import logging.config

LOG_CONFIG = {
    'version': 1,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - voice.%(module)s.%(funcName)s:%(lineno)d - %(levelname)s - %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'standard'
        },
        'timedRotatingFileHandler': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'level': 'DEBUG',
            'filename':'/home/circulus/log/app.log',
            'formatter': 'standard',
            'when': 'midnight',
            'interval': 1,
            'backupCount': 0,
            'encoding': 'utf8'
        }
    },
    'loggers': {
        'main': {
            'handlers': ['console','timedRotatingFileHandler'],
            'level':'DEBUG',
        },
        'controller': {
            'handlers': ['console','timedRotatingFileHandler'],
            'level':'DEBUG',
        },
        'logic': {
            'handlers': ['console','timedRotatingFileHandler'],
            'level':'DEBUG',
        },
        'util': {
            'handlers': ['console','timedRotatingFileHandler'],
            'level':'DEBUG',
        },
    }
}
def configure_logger(logger_type, api):
    LOG_CONFIG['handlers']['timedRotatingFileHandler']['filename'] = f'/home/circulus/log/app-{api}.log'
    logging.config.dictConfig(LOG_CONFIG)
    log = logging.getLogger(logger_type)
    log.propagate=0
    return log

if __name__ == "__main__":
    l = configure_logger('main')
    l.info("Hello world")
