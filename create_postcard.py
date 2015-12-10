#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
#
# Authors:
#   Michael Petretti <mic.petretti@gmail.com> - 2015
from pprint import pprint
import message_listing
import postcard


def ascii(file_path, address_name, street_and_number, postcode_and_city, country):
    """
    :param file_path: path to the text file you want to parse.
    :param address_name: see idea_layout.txt
    :param street_and_number: see idea_layout.txt
    :param postcode_and_city: see idea_layout.txt
    :param country: see idea_layout.txt
    :return: text file containing all the postcards
    """

    message_list = message_listing.build(file_path)

    postcard_layout = postcard.empty(address_name, street_and_number, postcode_and_city, country)

    formatted_message_list = message_listing.format_monospace_font(message_list)

    count = 0
    twelve_lines = list()
    postcard_stack = list()
    for number in range(len(formatted_message_list)):
        if count < 12:
            twelve_lines.append(formatted_message_list[number])
            count += 1
        if count == 12:
            postcard_stack.append(postcard.fill(twelve_lines, postcard_layout))
            count = 0
            twelve_lines = list()
    postcard_stack.append(postcard.fill(twelve_lines, postcard_layout))
    return postcard_stack

