#!/usr/bin/env python

import sys
import fileinput

uniquefiles={}
for line in fileinput.input():
	line=line.split('\t')
	key=line[0]
	filename=line[1]
	if key in uniquefiles:
		uniquefile[key]+='\n'+filename
	else:
		uniquefile[key]=filename	#dummy file as we jsut need key to exist
		print key+'\t'+filename 
