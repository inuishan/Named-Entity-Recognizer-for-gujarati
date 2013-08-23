import xml.etree.ElementTree as ET
import pprint

def prepareDictionary(f):
	tree = ET.parse(f)
	dic = {}
	for elem in tree.iter(tag='TEXT'):
		a = elem.attrib
		l = a.values()
		s = ''.join(l)
		t = elem.text
		print t		
		'''
		words = t.split()
		c = 0	
		for word in words:
			if c == 0:
				dic[word] = 'B'+'-'+s
			else:
				dic[word] = 'I'+'-'+s
			c = c + 1
		
		'''

g = open('1.xml','rb')
prepareDictionary(g)
