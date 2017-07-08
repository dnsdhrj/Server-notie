from configparser import ConfigParser
import shutil
import os

config = ConfigParser()
config.read(os.path.expanduser('~/records/notie/config.ini'))
feed_loc = os.path.expanduser(config['core']['DataLocation'] + config['email']['FeedLocation'])

row, column = shutil.get_terminal_size()
filled_column = 0

def _print(s):
    global filled_column
    filled_column += s.count('\n') + 1
    print(s)


def _draw_fill(c):
    count = int(row / len(c))
    rest = row - count*len(c)
    print(c * count, end='')
    _print(c[0:rest])


def _draw_center(s, head='', foot=''):
    start = int((row - len(s)) / 2)
    print(' ' * (start-1), end='')
    _print(head + s + foot)


def _display_email():
    display_list = [
        ('gmail', 'Gmail'),
        ('naver', 'Naver mail'),
        ('snu', 'MySNU mail'),
    ]
    notie_count = 0
    for filename, display_name in display_list:
        with open(os.path.join(feed_loc, filename)) as f:
            contents = f.readlines()
        if len(contents) != 0:  # Maybe BOM?
            _print('\t\033[33m{}\033[0;39m'.format(display_name))
            _print('-' * 25)
            for line in contents:
                splited = line.split('%%%%')
                print(splited[0], end='')
                _print('  \033[34m{}\033[0;39m'.format(splited[1]))
            notie_count += 1
    if notie_count == 0:
        _print('There\'s no email notification to show.')


def _display():
    _draw_fill('=')
    _draw_center('WELCOME', '\033[32m','\033[0;39m')
    _draw_fill('=')
    _print('')
    _display_email()
    _draw_fill('=')
    vacant_column = column - filled_column - 2
    if vacant_column > 0:
        print('\n' * vacant_column)


_display()
