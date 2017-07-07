from configparser import ConfigParser
import logging
import sys

if 'logger' not in globals():
    logger = logging.getLogger()
    logger.setLevel(logging.WARNING)

    config = ConfigParser()
    config.read('config.ini')
    log_loc = config['core']['LogLocation']
    handler = logging.FileHandler(log_loc)
    handler.setLevel(logging.WARNING)
    logger.addHandler(handler)


def notie_log(log, level='error'):
    if level == 'warning':
        logger.warning(log)
    elif level == 'critical':
        logger.critical(log)
    else:
        logger.error(log)


if __name__ == '__main__':  # Called from command line
    if sys.argc < 2:
        print('Please put log to the command line.')
        exit()
    notie_log(sys.argv[1])
