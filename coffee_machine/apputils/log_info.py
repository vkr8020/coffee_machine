import os
import logging
import logging.config


def load_logger_cfg(log_filename):
    """
    Load logger configuration
    :param log_filename:log filename
    :return:
    """
    d = {
        'version': 1,
        'formatters': {
            'simple': {
                'class': 'logging.Formatter',
                'format': '%(asctime)s - %(message)s'
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'INFO',
            },
            'file': {
                'class': 'logging.FileHandler',
                'filename': log_filename,
                'mode': 'w',
                'formatter': 'simple',
            },
        },
        'loggers': {
            '': {  # root logger
                'level': 'DEBUG',
                'handlers': ['console', 'file'],
                'propagate': False
            },
            'app_cfg': {
                'level': 'DEBUG',
                'handlers': ['file'],
                'propagate': False
            },
        }
    }

    logging.config.dictConfig(d)


def create_logger(logdir='logs', log_filename='sample'):
    """
    :param logdir: custom logdir name
    :param log_filename: custom log filename
    :return: logger
    """
    if not os.path.exists(logdir):
        os.makedirs(logdir)

    logfile = os.path.join(logdir, log_filename + '.log')
    load_logger_cfg(logfile)
    logger = logging.getLogger()
    logger.debug("Log file for this run: " + os.path.realpath(logfile))

    return logger
