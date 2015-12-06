import re
from pprint import pprint
import emoji

MESSAGE_REGEX = (r'(?P<day>[0-9]{2}[\/.][0-9]{2}[\/.][0-9]{2,4})[\s,]*([0-9]{2}:[0-9]{2}(:[0-9]{2})*)[\s:-]*'
                 r'(?P<person>[^:]*):\s(?P<message>.*)')
DATE_REGEX = r'(?P<day>[0-9]{2}[\/.][0-9]{2}[\/.][0-9]{2,4})[\s,]*([0-9]{2}:[0-9]{2}(:[0-9]{2})*)'


def read_file(filename):
    """ Read a messages file and returns a list of lines
    :param filename: file to read
    :return: list of lines with special chars filtered out
    """
    with open(filename, 'r') as f:
        lines = f.readlines()

    result = []
    i = 0
    for line in lines:
        if line != '\n':
            line = line.rstrip('\n').rstrip('\r\r')
            if re.search(DATE_REGEX, line) is not None:
                i += 1
                result.append(line)
            else:
                result[i-1] = result[i-1] + ' ' + line
    return result


def parse_message(lines):
    """ Divide the message into its components using a regex
    :param lines: list of lines to parse
    :return: list of tuples containing the different parts of the message
    """
    struct = []
    for line in lines:
        line = emoji.demojize(line.decode('utf-8'))
        match = re.match(MESSAGE_REGEX, line)
        if not match:
            continue
        date = match.group('day')
        day = date[0:2]
        month = date[3:5]
        year = date[6:]
        new_date = '{}/{}/{}'.format(year, month, day)
        struct.append((new_date, match.group('person'), match.group('message'), ))
    return struct


def format_parsed(messages):
    """ Group the messages by date
    :param messages: list of tuples containing the parts of the messages
    :return: dict with days as keys and list of tuples containing messages
    """
    struct = dict()
    for line in messages:
        if line[0] in struct:
            struct[line[0]].append((line[1], line[2], ))
        else:
            struct[line[0]] = list()
            struct[line[0]].append((line[1], line[2], ))
    return struct


def parser(file='messages.txt'):
    """ Main function that parses a file
    :param file: filename to parse
    :return: final dict with the messages grouped by date
    """
    lines = read_file(file)
    messages = parse_message(lines)
    return format_parsed(messages)

if __name__ == '__main__':
    pprint(parser('small.txt'))
