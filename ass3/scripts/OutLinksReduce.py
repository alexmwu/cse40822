#!/usr/bin/env python

import sys
import fileinput

uniquefiles={}
for line in fileinput.input():
	line=line.split('\t')
	filename=line[0]
	key=line[1]
	if key in uniquefiles:
		continue
	else:
		uniquefile[key]=1	#dummy file as we jsut need key to exist
		print filename+'\t'+key 
