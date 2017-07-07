import sys

from mail.blacklist import add_blacklist, remove_blacklist, show_blacklist
from mail.feed import clear_feed

argc = len(sys.argv)
if argc < 2 or sys.argv[1] == '--help':
    print('Commands list:')
    print('  blackadd')
    print('  blackdel')
    print('  blacklist')
    print('  clearemail')
    exit()


command = sys.argv[1]
if command == 'blackadd':
    if argc < 3:
        print('Put arguments to add to email blacklist.')
        exit()
    for word in sys.argv[2:argc]:
        add_blacklist(word)
        print('Added \'{}\' to the blacklist.'.format(word))
elif command == 'blackdel':
    if argc < 3:
        print('Put arguments to delete in email blacklist.')
        exit()
    for word in sys.argv[2:argc]:
        remove_blacklist(word)
        print('Deleted \'{}\' from the blacklist.'.format(word))
elif command == 'blacklist':
    print(show_blacklist())
elif command == 'clearemail':
    clear_feed()
