#!/usr/bin/env python3.5
# -*- coding: utf-8
import pprint
import random

import unittest
import create_postcard
import message_listing


class TestPostcard(unittest.TestCase):

    def test_format_monospace_date(self):
        test_list = [('date', '[29.06.2015]')]
        text_width = random.randint(30,50)
        result_list = message_listing.format_monospace_font(test_list, text_width)
        self.assertEqual(len(result_list), 2)
        self.assertEqual(len(result_list[0]), text_width)
        self.assertEqual(len(result_list[1]), text_width)
        blank_line = ''
        for _ in range(text_width):
            blank_line = blank_line + ' '
        self.assertEqual(result_list[0], blank_line)
        date_line = '     [29.06.2015]'
        for _ in range(text_width - 17):
            date_line = date_line + ' '
        self.assertEqual(result_list[1], date_line)

    def test_format_monospace_short_person1(self):
        test_list = [(True, 'just a few chars')]
        text_width = random.randint(30,50)
        result_list = message_listing.format_monospace_font(test_list, text_width)
        self.assertEqual(len(result_list), 1)
        self.assertEqual(len(result_list[0]), text_width)
        short_line = '->just a few chars'
        for _ in range(text_width - 18):
            short_line = short_line + ' '
        self.assertEqual(result_list[0], short_line)

    def test_format_monospace_short_person2(self):
        test_list = [(False, 'just a few chars')]
        text_width = random.randint(30,50)
        result_list = message_listing.format_monospace_font(test_list, text_width)
        self.assertEqual(len(result_list), 1)
        self.assertEqual(len(result_list[0]), text_width)
        short_line = 'just a few chars<-'
        for _ in range(text_width - 18):
            short_line = ' ' + short_line
        self.assertEqual(result_list[0], short_line)
    # def test_format_monospace_short_false(self):
    # def test_format_monospace(self):
    # def test_format_monospace(self):
    # def test_format_monospace(self):


def test_output():
    all_postcards = create_postcard.ascii('messages.txt', 'Liebe Kathi', 'Ferne Stadt', 'Deinestrasse 17', 'Kaltes Deutschland')
    file = open('output.txt', 'w')
    for postcard in all_postcards:
        file.writelines('\n')
        for line in postcard:
            file.writelines(line + '\n')



if __name__ == '__main__':
    test_output()
