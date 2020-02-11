import os

from notie.mail.config import config


def clear_feed():
    feed_loc = config['feed_loc']
    file_list = os.listdir(feed_loc)
    for filename in file_list:
        open(os.path.join(feed_loc, filename), 'w').close()
