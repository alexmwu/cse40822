#!/usr/bin/env python

import fileinput
import sys
import re

filterout=['doctype','html','head','meta','script','style','body','div','span','href','img','class','table','tbody','thead','tfoot','form','input','code','button','caption','cite','col','pre','javascript','function','menu','stylesheet','css','the','src','and','alt','width','this','amp','height','images','sites','document']	#uninteresting words/html tags


words={}
lastword=0
for line in fileinput.input():
	line=re.sub("[^\w]"," ",line)
	line=line.strip()
	line=line.split()
	for word in line:
		if lastword==0:
			lastword=word
			continue
		if len(str(word))<3:
			continue
		if word in filterout:
			continue
		word=word.lower()
		key=lastword+' '+word
		if word in words.keys():
			words[key]+=1
		else:
			words[key]=1
		lastword=word
for key in words:
	print key+'\t'+str(words[key])
	


