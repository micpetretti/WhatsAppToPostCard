#!/usr/bin/env python3.5
# -*- coding: utf-8
import pprint

import unittest
import create_postcard
import message_listing


class TestPostcard(unittest.TestCase):

    def test_format_monospace_date(self):
        test_list = [('date', '[29.06.2015]')]
        result_list = message_listing.format_monospace_font(test_list)
        self.assertEqual(len(result_list), 2)
        self.assertEqual(len(result_list[0]), 40)
        self.assertEqual(len(result_list[1]), 40)
        self.assertEqual(result_list[0], '                                        ')
        self.assertEqual(result_list[1], '     [29.06.2015]                       ')

    def test_format_monospace_short_person1(self):
        test_list = [(True, 'this is a string with few chars')]
        result_list = message_listing.format_monospace_font(test_list)
        self.assertEqual(len(result_list), 1)
        self.assertEqual(len(result_list[0]), 40)
        self.assertEqual(result_list[0], '->this is a string with few chars       ')

    def test_format_monospace_short_person2(self):
        test_list = [(False, 'this is a string with few chars')]
        result_list = message_listing.format_monospace_font(test_list)
        self.assertEqual(len(result_list), 1)
        self.assertEqual(len(result_list[0]), 40)
        self.assertEqual(result_list[0], '       this is a string with few chars<-')
    # def test_format_monospace_short_false(self):
    # def test_format_monospace(self):
    # def test_format_monospace(self):
    # def test_format_monospace(self):


def test_output():
    pprint.pprint(create_postcard.ascii('messages.txt', 'saf', 'afe', 'afrgfsdaa', 'qefrgw'))

if __name__ == '__main__':
    test_output()
