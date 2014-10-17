#!/usr/bin/env python

import sys
import re
import fileinput


filename=os.getenv('mapreduce_map_input_file')

for line in fileinput.input():
	match=re.search("<.*a\ *href\ *=\ *.*>.*</\ *a\ *>",line)	#find all instances of a href tags
	if match!=None:	#if match
		line=match.group(0)
		line=line.replace("'",'"')
		line=line.split('"')
		for substr in line:
			if "http://" in substr:
				substr=substr.strip("http://")
				substr=substr.split('/',1)[0]
				substr="http_"+substr
				print substr+'\t'+filename
