#!/usr/bin/env python3

import unittest
from filterRSS import *

class TestFilterRSS(unittest.TestCase):

	def test_get_count(self):
		s1 = "header<item>111</item><item>222</item>footer"
		s2 = "header footer"

		self.assertEqual(get_count(s1), 2)
		self.assertEqual(get_count(s2), 0)


	def test_get_header_footer(self):
		s = "header<item>111</item><item>222</item>footer"
		
		self.assertEqual(get_header(s), "header")
		self.assertEqual(get_footer(s), "footer")

	def test_get_items(self):
		s = "header<item>111</item><item>222</item>footer"

		self.assertEqual(get_items(s), ["111", "222"])

	def test_get_tag_content(self):
		s = "123<xx a='b'>4<z>56</z>78</xx>9"

		self.assertEqual(get_tag_content(s, "xx"),"4<z>56</z>78")
		self.assertEqual(get_tag_content(s, "y"),  "")
		self.assertEqual(get_tag_content(s, "z"),  "56")






if __name__ == "__main__":
	unittest.main()
