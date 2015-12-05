import re
import json
from collections import OrderedDict

MESSAGE_REGEX = (r'(?P<day>[0-9]{2}\/[0-9]{2}\/[0-9]{2})\s(?P<hour>[0-9]{2}:[0-9]{2}:[0-9]{2}):\s'
                 r'(?P<person>[^:]*):\s(?P<message>.*)')


def read_file(filename):
    """
    :param filename:
    :return:
    """
    with open(filename, 'r') as f:
        lines = f.readlines()

    result = []
    for line in lines:
        if line != '\n':
            line = line.rstrip('\n')
            result.append(line)
    return result


def parse_message(lines):
    """
    :param lines:
    :return:
    """
    struct = []
    for line in lines:
        match = re.match(MESSAGE_REGEX, line)
        if not match:
            break
        struct.append((match.group('day'), match.group('person'), match.group('message'), ))
    return struct


def format_parsed(messages):
    """
    :param messages:
    :return:
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
    """
    :param file:
    :return:
    """
    lines = read_file(file)
    messages = parse_message(lines)
    return format_parsed(messages)

if __name__ == "__main__":
    print(parser('messages_small.txt'))
