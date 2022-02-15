#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome


import sys
import random

# command line input
genome_size = int(sys.argv[1])
read_number = int(sys.argv[2])
read_length = int(sys.argv[3])

# create empty genome, fill with random reads and count them
genome= [0]*genome_size
for i in range(read_number):	
	r = random.randint(0, genome_size - read_length)
	for j in range(read_length):
		genome[j + r] += 1

# define min and max
min = genome[read_length]
max = genome[read_length]

#avg coverage
read = 0
# start looking at genome after first nt defined by the read length 
# and before last nts defined by the read length

for x in genome[read_length:-read_length]: 
	if x < min: min = x
	if x > max: max = x
	read += x 
print(min, max, f'{read/(genome_size - 2*read_length):.5f}')


# Worked with Krikor
"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
