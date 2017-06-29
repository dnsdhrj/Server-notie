from configparser import ConfigParser
import os


config = ConfigParser()
config.read('../config.ini')
feed_loc = config['core']['DataLocation'] + config['email']['FeedLocation']


def clear_feed():
    file_list = os.listdir(feed_loc)
    for filename in file_list:
        open(os.path.join(feed_loc, filename), 'w').close()
