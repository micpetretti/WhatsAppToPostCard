#!/usr/bin/env python3.5
# coding=utf-8
#
# Authors:
#   Jorge Dominguez <jorgedc93@gmail.com> - 2015
import re
import emoji

MESSAGE_REGEX = (r'(?P<day>[0-9]{2}[\/.][0-9]{2}[\/.][0-9]{2,4})[\s,]*([0-9]{2}:[0-9]{2}(:[0-9]{2})*)[\s:-]*'
                 r'(?P<person>[^:]*):\s(?P<message>.*)')
DATE_REGEX = r'(?P<day>[0-9]{2}[\/.][0-9]{2}[\/.][0-9]{2,4})[\s,]*([0-9]{2}:[0-9]{2}(:[0-9]{2})*)'

REMOVE_MODIFIERS = r'(.*?)(:emoji_modifier_fitzpatrick_type-[0-9]:)(.*)'


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
            # If the new line is not a new message we append this line to the previous one
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
        # We convert the emojis to text representation for easier handling
        line = emoji.demojize(line)
        match_message = re.match(MESSAGE_REGEX, line)
        if not match_message:
            continue
        message = match_message.group('message')
        match = re.match(REMOVE_MODIFIERS, message)
        if match:
            message = match.group(1) + '' + match.group(3)
        date = match_message.group('day')
        # We need to change the date from DD/MM/YY to YY/MM/DD for easier sorting
        day = date[0:2]
        month = date[3:5]
        year = date[6:]
        new_date = '{}/{}/{}'.format(year, month, day)
        struct.append((new_date, match_message.group('person'), message))
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
