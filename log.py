from configparser import ConfigParser
import logging
import sys
import os

if 'logger' not in globals():
    logger = logging.getLogger()
    logger.setLevel(logging.WARNING)

    config = ConfigParser()
    config.read(os.path.expanduser('~/records/notie/config.ini'))
    log_loc = os.path.expanduser(config['core']['LogLocation'])
    handler = logging.FileHandler(log_loc)
    handler.setLevel(logging.WARNING)

    formatter = logging.Formatter('%(asctime)s  (%(levelname)s)  %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def notie_log(log, level='error'):
    if level == 'warning':
        logger.warning(log)
    elif level == 'critical':
        logger.critical(log)
    else:
        logger.error(log)


if __name__ == '__main__':  # Called from command line
    if len(sys.argv) < 2:
        print('Please put log to the command line.')
        exit()
    notie_log(sys.argv[1])
