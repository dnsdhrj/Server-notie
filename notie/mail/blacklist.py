from notie.mail.config import config


def add_blacklist(word):
    with open(config['blacklist_loc'], 'r', encoding='utf8') as f:
        if len(f.read(3)) < 3:
            firstline = True
        else:
            firstline = False
    with open(config['blacklist_loc'], 'a', encoding='utf8') as f:
        if firstline:
            f.write(word)
        else:
            f.write('\n' + word)


def remove_blacklist(word):
    with open(config['blacklist_loc'], 'r', encoding='utf8') as f:
        blacklist = f.readlines()
        blacklist = [x for x in blacklist if x != word]
    with open(config['blacklist_loc'], 'w+', encoding='utf8') as f:
        f.seek(0, 0)
        f.write(u'\n'.join(blacklist))


def show_blacklist():
    with open(config['blacklist_loc'], 'r', encoding='utf8') as f:
        return f.read()

