#!/usr/bin/env python

import os
import fileinput
import sys
import re

filterout=['doctype','html','head','meta','script','style','body','div','span','href','img','class','table','tbody','thead','tfoot','form','input','code','button','caption','cite','col','pre','javascript','function','menu','stylesheet','css','the','src','and','alt','width','this','amp','height','images','sites','document']	#uninteresting words/html tags

filename=os.getenv('mapreduce_map_input_file')
filename=filename.split('/')
filename=filename[len(filename)-1]
words={}

for line in fileinput.input():
	line=re.sub("[^\w]"," ",line)
	line=line.strip()
	line=line.split()
	#filename=fileinput.filename()
	#filename=filename.split('/')
	#filename=filename[len(filename)-1]
	for word in line:
		if len(str(word))<3:
			continue
		if word in filterout:
			continue
		key=word.lower()
		print key+'\t'+filename
	

#		if word in words.keys():
#			continue
#		else:
#			words[word]=filename
#for key in words:
#	print key+'\t'+str(words[key])
	


