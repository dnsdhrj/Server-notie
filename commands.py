import sys

from mail.blacklist import add_blacklist, remove_blacklist
from mail.feed import clear_feed

argc = len(sys.argv)
if argc <= 2 or sys.argv[1] == '--help':
    print('Commands list:')
    print('  blackadd')
    print('  blackdel')
    print('  clearemail')
    exit()


command = sys.argv[1]
if command == 'blackadd':
    if argc <= 3:
        print('Put arguments to add to email blacklist.')
        exit()
    for word in sys.argv[2:argc]:
        add_blacklist(word)
elif command == 'blackdel':
    if argc <= 3:
        print('Put arguments to delete in email blacklist.')
        exit()
    for word in sys.argv[2:argc]:
        remove_blacklist(word)
elif command == 'clearemail':
    clear_feed()
