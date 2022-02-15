#!/usr/bin/env python3

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# E.g. python3 entropy.py 0.4 0.3 0.2 0.1
# Put the probabilities into a new list
# Don't forget to convert them to numbers

import math
import sys

p =[]
sum = 0
tolerance = 0.01

#turn prb into list also turn to float
for i in range(1, len(sys.argv)):
	p.append(float(sys.argv[i]))

#check for sum = 1
sum += float(sys.argv[i])
if abs(sum -1.0) > tolerance:
	sys.exit()
	
#entropy calculation
entropy = 0
for i in range(len(p)):
	entropy -= p[i] * math.log2(p[i])
print(f'{entropy:.3f}')


# Worked with Krikor
"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
