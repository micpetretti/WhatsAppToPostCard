#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
#
# Authors:
#   Michael Petretti <mic.petretti@gmail.com> - 2015

import parser


def builder(path_to_file):
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
        message_list.append((alignment, '[' + day + '.' + month + '.' + year + ']'))
        daily_messages = message_dict[date]
        for message in daily_messages:
            new_sender = message[0]
            if not last_sender == new_sender:
                alignment = not alignment
                last_sender = new_sender
            message_list.append((alignment, message[1]))

    return message_list

def readable_date(date):
    y, m, d = date.split('/')
    return y, m, d

