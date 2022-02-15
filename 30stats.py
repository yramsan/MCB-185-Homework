#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

import sys
import math

#turn list to float
p = []
for i in range(1, len(sys.argv)):
	p.append(float(sys.argv[i]))

#count variables in list
count = 0 
for i in range(len(p)):
	count += p[i]
print('Count:', len(p))

#get min and max
p.sort()
min = p[0]
max = p[-1]
print('Minimum:', min) 
print('Maximum:', max) 

#calc. mean
sum = 0
for j in range(len(p)):
    sum = sum + p[j]
mean = sum/len(p)
print('Mean:', f'{mean:.3f}')

#calc. std dev
stdev = 0 
sum = 0 
for i in range(len(p)):
	sum += (p[i]- mean)**2
	stdev = math.sqrt((sum)/(len(p)))
print('Std. dev:', f'{stdev:.3f}')

#calc. median
if len(p) % 2 == 0: 
	med_1= len(p)//2 
	med_2= len(p)//2 -1
	med= (p[med_1] + p[med_2])/2
	print('Median:', f'{med:.3f}')
else:
	med= len(p)//2
	print('Median:', f'{med:.3f}')
	
# Worked with Krikor 
"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""

