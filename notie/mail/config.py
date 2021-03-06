from configparser import ConfigParser
import os

if 'config' not in globals():
    config = {}
    _configs = ConfigParser()
    _configs.read('config.ini')
    if 'email' not in _configs:
        _configs.read(os.path.expanduser('~/data/services/notie/config.ini'))
    config['feed_loc'] = os.path.expanduser(os.path.join(_configs['core']['DataLocation'], _configs['email']['FeedLocation']))
    config['inbox_loc'] = os.path.expanduser(_configs['email']['InboxLocation'])
    config['blacklist_loc'] = os.path.expanduser(os.path.join(_configs['core']['DataLocation'], _configs['email']['BlacklistFile']))
