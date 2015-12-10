#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
#
# Authors:
#   Michael Petretti <mic.petretti@gmail.com> - 2015

def format_string(string):
    """ Fill string with whitespaces to the right and cut to length 18 """
    string = string + '                  '
    return string[:18]


def empty(name=None, street=None, city=None, country=None):
    """
    return postcard layout with recipients fields filled as list
    :param name: recipient name
    :param street: recipient street
    :param city: recipient city
    :param country: recipient country
    :return: list with lines of the postcard
    """

    empty_postcard = \
"""--------------------------------------------------------------------
|                                         |                 #####  |
|                                         |                 #####  |
|                                         |                 #####  |
|                                         |                        |
|                                         |                        |
|                                         |                        |
|                                         |  NAME             .    |
|                                         |                        |
|                                         |  STREET           .    |
|                                         |                        |
|                                         |  CITY             .    |
|                                         |                        |
|                                         |  COUNTRY          .    |
|                                         |                        |
--------------------------------------------------------------------""".split('\n')

    if name:
        name = format_string(name)
        empty_postcard[7] = empty_postcard[7].replace('NAME             .', name)
    if street:
        street = format_string(street)
        empty_postcard[9] = empty_postcard[9].replace('STREET           .', street)
    if city:
        city = format_string(city)
        empty_postcard[11] = empty_postcard[11].replace('CITY             .', city)
    if country:
        country = format_string(country)
        empty_postcard[13] = empty_postcard[13].replace('COUNTRY          .', country)

    return empty_postcard

def fill(twelve_lines, postcard, number=None):
    """
    The empty textfield can take 12 lines with 40 chars each. fills the postcard with content.
    :param twelve_lines: expects list with 12 lines of 40 chars each
    :param postcard: the postcard where the 12 lines should be filled in to
    :param number: the count of which postcard it is.
    :return: filled and numbered postcard as list of strings
    """
    line_count = 2
    for line in twelve_lines:
        postcard[line_count] = postcard[line_count].replace('                                         ', line)
        line_count += 1
    return postcard

