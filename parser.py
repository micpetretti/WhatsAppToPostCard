import re

MESSAGE_REGEX = (r'(?P<day>[0-9]{2}[\/.][0-9]{2}[\/.][0-9]{2,4})[\s,]*([0-9]{2}:[0-9]{2}(:[0-9]{2})*)[\s:-]*'
                 r'(?P<person>[^:]*):\s(?P<message>.*)')


def read_file(filename):
    """ Read a messages file and returns a list of lines
    :param filename: file to read
    :return: list of lines with special chars filtered out
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
    """ Divide the message into its components using a regex
    :param lines: list of lines to parse
    :return: list of tuples containing the different parts of the message
    """
    struct = []
    for line in lines:
        match = re.match(MESSAGE_REGEX, line)
        if not match:
            continue
        struct.append((match.group('day'), match.group('person'), match.group('message'), ))
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
