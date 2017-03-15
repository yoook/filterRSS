#!/usr/bin/env python3

import subprocess
import unittest


class TestFilterRSS(unittest.TestCase):

	def setUp(self):
		self.instring = """header
<item>1 Sport <link>http://www1.sportschau.de/</link></item>
<item>2 Sport <link>http://www.sportschau.de/</link></item>
<item>3 Regionalsport <link>http://www.tagesschau.de/ardimport/sport/</link></item>
<item>4 Ausland <link>http://www.tagesschau.de/ausland/</link></item>
<item>5 Inland <link>http://www.tagesschau.de/inland/</link></item>
<item>6 Kultur <link>http://www.tagesschau.de/kultur/</link></item>
<item>7 Regional <link>http://www.tagesschau.de/ardimport/regional/</link></item>
<item>8 Videoblog <link>http://www.tagesschau.de/videoblog/</link></item>
<item>9 anderes <link>something-diffeent</link></item>
<item>10 Regional2 <link>http://www.rbb-online.de/123</link></item>
<item>11 Regionalsport2 <link>http://www.rbb-online.de/sport/345</link></item>
footer\n"""

		#array containing the lines of instring
		self.instringArray=self.instring.split('\n')
		
		#select elements to be in the array
		self.instringSubArray = lambda t: [self.instringArray[i] for i in t]
		
		#no need to select header and footer, convert back to string
		self.subInstring = lambda t:'\n'.join(self.instringSubArray([0]+list(t)+[-2, -1]))


	def test_all_but_sport(self):
		p = subprocess.Popen(['./filterRSS.py', 'filterTagesschau', 'alles'],
			stdin=subprocess.PIPE,
			stdout=subprocess.PIPE,
			stderr=subprocess.STDOUT
		)
		o, e = p.communicate(self.instring.encode('utf-8'))
		should = self.subInstring([4,5,6,7,8,9,10])
		self.assertEqual(o, should.encode('utf-8'), "\n\noutput:\n"+o.decode('utf-8')+"\nshould be:\n"+should)	

	def test_Ausland_Inland_Kultur(self):
		p = subprocess.Popen(['./filterRSS.py', 'filterTagesschau', 'Kultur', 'Ausland', 'Inland'],
			stdin=subprocess.PIPE,
			stdout=subprocess.PIPE,
			stderr=subprocess.STDOUT
		)
		o, e = p.communicate(self.instring.encode('utf-8'))
		should = self.subInstring([4,5,6])
		self.assertEqual(o, should.encode('utf-8'), "\n\noutput:\n"+o.decode('utf-8')+"\nshould be:\n"+should)

	def test_Regional_Videoblog_nonsense(self):
		p = subprocess.Popen(['./filterRSS.py', 'filterTagesschau', 'Videoblog', 'Regional', 'nonsense'],
			stdin=subprocess.PIPE,
			stdout=subprocess.PIPE,
			stderr=subprocess.STDOUT
		)
		o, e = p.communicate(self.instring.encode('utf-8'))
		should = self.subInstring([7,8,10])
		self.assertEqual(o, should.encode('utf-8'), "\n\noutput:\n"+o.decode('utf-8')+"\nshould be:\n"+should)

	def test_anderes(self):
		p = subprocess.Popen(['./filterRSS.py', 'filterTagesschau', 'anderes'],
			stdin=subprocess.PIPE,
			stdout=subprocess.PIPE,
			stderr=subprocess.STDOUT
		)
		o, e = p.communicate(self.instring.encode('utf-8'))
		should = self.subInstring([9])
		self.assertEqual(o, should.encode('utf-8'), "\n\noutput:\n"+o.decode('utf-8')+"\nshould be:\n"+should)

if __name__ == "__main__":
		
	unittest.main()
