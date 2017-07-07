from configparser import ConfigParser
import os

if 'config' not in locals():
    config = {}
    _configs = ConfigParser()
    _configs.read('../config.ini')
    config['feed_loc'] = os.path.join(_configs['core']['DataLocation'], _configs['email']['FeedLocation'])
    config['inbox_loc'] = _configs['email']['InboxLocation']
    config['blacklist_loc'] = os.path.join(_configs['core']['DataLocation'], _configs['email']['BlacklistFile'])
