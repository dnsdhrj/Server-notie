import click

from mail.blacklist import add_blacklist, remove_blacklist, show_blacklist
from mail.feed import clear_feed


@click.group()
def cli():
    pass


@cli.command(help='Add words to email blacklist.')
@click.argument('words', required=True, nargs=-1)  # varargs
def blackadd(words):
    for word in words:
        add_blacklist(word)
        print('Added \'{}\' to the blacklist.'.format(word))


@cli.command(help='Delete words in email blacklist.')
@click.argument('words', required=True, nargs=-1)  # varargs
def blackdel(words):
    for word in words:
        remove_blacklist(word)
        print('Added \'{}\' to the blacklist.'.format(word))


@cli.command(help='Show blacklisted words.')
def blacklist():
    print(show_blacklist())


@cli.command(help='Clear all email notifications.')
def clearemail():
    clear_feed()


if __name__ == '__main__':
    cli()

