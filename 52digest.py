#!/usr/bin/env python3
# 52digest.py

import re
import sys

# Write a program that performs an EcoRI digest on the SARS-COV2 genome
# The program should have 2 arguments
#    1. The genome file
#    2. The restriction pattern
# The output should be the sizes of the restriction fragments
# reading the file

filename = sys.argv[1]
site = sys.argv[2]

def readfile(filename):
	with open(filename) as fp:
		seq = ''
		flag_origin = False
		for line in fp.readlines():
			if 'ORIGIN' in line:
				flag_origin = True
				continue
			if flag_origin:
				words = line.split()
				for word in words[1:]:
					seq += word
	return seq

fragments = digest(sys.argv[1], sys.argv[2])
if __name__ == '__main__':
	for i in range(len(fragments)-1):
		fragment_length = fragments[i + 1] - fragments[i]
		print(fragment_length)


"""
python3 52digest.py ../Data/sars-cov2.gb gaattc
1160
10573
5546
448
2550
2592
3569
2112
1069
"""
