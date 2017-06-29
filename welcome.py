from configparser import ConfigParser
import shutil
import os

config = ConfigParser()
config.read('./config.ini')
feed_loc = config['core']['DataLocation'] + config['email']['FeedLocation']
row, column = shutil.get_terminal_size()


def _draw_fill(c):
    count = int(row / len(c))
    rest = row - count*len(c)
    print(c * count, end='')
    print(c[0:rest])


def _draw_center(s):
    start = int((row - len(s)) / 2)
    print(' ' * (start-1), end='')
    print(s)


def _display_email():
    display_list = [
        ('gmail', 'Gmail'),
        ('naver', 'Naver mail'),
        ('snu', 'MySNU mail'),
    ]
    for filename, display_name in display_list:
        with open(os.path.join(feed_loc, filename)) as f:
            contents = f.read()
        if len(contents) <= 2:  # Maybe BOM?
            print('\t' + display_name)
            print('-' * 15)
            print(contents)


def _display():
    _draw_fill('=')
    _draw_center('Welcome')
    _draw_fill('=')
    _display_email()
    _draw_fill('=')


_display()
