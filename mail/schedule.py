import time
import os

from mail.config import config
from mail.emailparser import parse_email

# prerequisite: new emails should be in inbox using 'getmail'

blacklist = None


def _add_email_feed(file_loc, service_name):
    email_info = parse_email(file_loc)
    if email_info is None:
        return
    if any(substr in email_info['From'] for substr in blacklist):
        return
    if any(substr in email_info['Subject'] for substr in blacklist):
        return
    with open(os.path.join(config['feed_loc'], service_name), 'a', encoding='utf8') as f:
        line = '{}\t{}\n'.format(email_info['Subject'], email_info['From'])
        f.write(line)


def _refresh_email_feed(service_name):
    inbox_loc = config['inbox_loc']
    latest_file_loc = os.path.join(inbox_loc, service_name, 'latest')
    if os.path.isfile(latest_file_loc):
        with open(latest_file_loc) as f:
            recent_updated_str = f.read()
            recent_updated = time.mktime(time.strptime(recent_updated_str, '%Y:%m:%d:%H:%M:%S'))
    else:
        recent_updated = time.mktime(time.strptime('2000:01:01:00:00:00', '%Y:%m:%d:%H:%M:%S'))
    
    service_loc = os.path.join(inbox_loc, service_name, 'new')
    for filename in os.listdir(service_loc):
        if filename == 'latest':
            continue
        file_loc = os.path.join(service_loc, filename)
        if os.path.getmtime(file_loc) > recent_updated:
            _add_email_feed(file_loc, service_name)

    with open(latest_file_loc, 'w') as f:
        recent_updated_str = time.strftime('%Y:%m:%d:%H:%M:%S')
        f.write(recent_updated_str)


def do_schedule():
    global blacklist
    with open(config['blacklist_loc']) as file:
        blacklist = file.readlines()
    for service in os.listdir(config['inbox_loc']):
        _refresh_email_feed(service)
