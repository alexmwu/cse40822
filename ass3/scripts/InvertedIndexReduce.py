#!/usr/bin/env python

import fileinput
import operator

uniquekeys={}	#check for unique filenames for the word output
for line in fileinput.input():
	line=line.strip()
	line=line.split('\t')
	key=line[1]
	#key=line.split('/')
	#key=key[len(key)-1]
	word=line[0]
	if key in uniquekeys:
		continue
	else:
		uniquekeys[key]=1	#dummy assignment to make sure key exists
		print word+'\t'+key

#	line=line.strip()
#	line=line.split('\t')
#	key=line[0]
#	value=line[1]
#	print key+'\t'+value

#	if key in reducedcount:
#		reducedcount[key]+=int(value)
#	else:
#		reducedcount[key]=int(value)
#reducedcount=sorted(reducedcount.items(),key=operator.itemgetter(1),reverse=True)
#for i in range(len(reducedcount)):
#	print reducedcount[i][0]+'\t'+str(reducedcount[i][1]);
