from email.parser import Parser
from email.header import decode_header

from log import notie_log


def _decode_header_unicode(s):
    return u''.join(
        word.decode(encoding or 'utf8') if isinstance(word, bytes) else word
        for word, encoding in decode_header(s))


def parse_email(filename):
    parser = Parser()
    with open(filename) as file:
        try:
            header = parser.parse(file, headersonly=True)
        except UnicodeDecodeError:
            notie_log('[emailparser] Ignored mail with strange encoding: {}'.format(filename))
            return None
    decode_list = [
        'From',
        'Subject',
    ]
    return {item: _decode_header_unicode(header.get(item)) for item in decode_list}
