from mail.config import config


def add_blacklist(word):
    with open(config['blacklist_loc'], 'a', encoding='utf8') as f:
        f.write(word)


def remove_blacklist(word):
    with open(config['blacklist_loc'], 'w', encoding='utf8') as f:
        blacklist = f.readlines()
        blacklist = [x for x in blacklist if x != word]
        f.seek(0, 0)
        f.write(u'\n'.join(blacklist))
