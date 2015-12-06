#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
#
# Authors:
#   Michael Petretti <mic.petretti@gmail.com> - 2015


def create_postcard(file_path, address_name, street_and_number, postcode_and_city, country):
    """
    :param file_path: path to the text file you want to parse.
    :param address_name: see idea_layout.txt
    :param street_and_number: see idea_layout.txt
    :param postcode_and_city: see idea_layout.txt
    :param country: see idea_layout.txt
    :return: text file containing all the postcards
    """

    # parse the txt into memory as a list and replace emoji unicode chars

    # parse the list into into the format of the postcard
    #   - define the empty postcard as list of strings
    #   - put the recipient in the fields
    #   - use the conversation and replace the empty places
    #   - group them under headlines of date and by one sender on each own side
    #   - enumerate the postcards
    #   -

    # write to file
