#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
#
# Authors:
#   Michael Petretti <mic.petretti@gmail.com> - 2015

import parser


def build(path_to_file):
    """
    Builds a list of lines grouped by date and person
    :return:
    """
    message_dict = parser.parser(path_to_file)
    date_list = sorted(message_dict.keys())
    message_list = list()

    last_sender = ""
    alignment = True

    # for readability later formatting has to happen, one person will be aligned left, one to the right.
    # if field of the tupels in list is true it means message is to be aligned left, False -> to the right
    for date in date_list:
        year, month, day = readable_date(date)
        message_list.append(('date', '[' + day + '.' + month + '.' + year + ']'))
        daily_messages = message_dict[date]
        for message in daily_messages:
            new_sender = message[0]
            if not last_sender == new_sender:
                alignment = not alignment
                last_sender = new_sender
            message_list.append((alignment, message[1]))
    return message_list


def format_monospace_font(message_list):
    """ In order to enter it to the empty postcard layout every line must be 40 chars and padded for readability.
    :param message_list:
    :return: list of 40 char strings
    """
    formatted_list = list()
    for tupel in message_list:
        # if date, print in the middle
        # check that it fitts in line
        # check person and add padding
        if isinstance(tupel[0], str):
            line = '                                         '
            formatted_list.append(line)
            line = '     ' + tupel[1] + '                                   '
            line = line[0:41]
            formatted_list.append(line)
        else:
            words = tupel[1].split(' ')
            num_letters = 0
            line = ''
            message_line_split = list()
            for word in words:
                if num_letters + len(word) <= 36:
                    line = line + word + ' '
                    num_letters = num_letters + len(word) + 1
                else :
                    message_line_split.append(line)
                    num_letters = len(word) + 1
                    line = word + ' '
            message_line_split.append(line)
            for message in message_line_split:
                if tupel[0] is True:
                    message = '->' + message + '                                        '
                    formatted_list.append(message[:41])
                if tupel[0] is False:
                    message = message.rstrip(' ')
                    for _ in range(39 - len(message)):
                        message = ' ' + message
                    message = message + '<-'
                    formatted_list.append(message)
    return formatted_list


def readable_date(date):
    y, m, d = date.split('/')
    return y, m, d

