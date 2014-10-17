#!/usr/bin/env python

import fileinput
import operator

reducedcount={}
for line in fileinput.input():
	line=line.strip()
	line=line.split('\t')
	key=line[0]
	value=line[1]
	if key in reducedcount:
		reducedcount[key]+=int(value)
	else:
		reducedcount[key]=int(value)
reducedcount=sorted(reducedcount.items(),key=operator.itemgetter(1),reverse=True)
for i in range(10):
	print reducedcount[i][0]+'\t'+str(reducedcount[i][1]);
