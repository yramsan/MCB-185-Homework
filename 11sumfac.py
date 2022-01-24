#!/usr/bin/env python3

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# No, you may not use math.factorial()
# Use the same loop for both calculations

n = 5

# your code goes here

runsum = n
fact = n 

for i in range (1, n): 
	runsum += i
	fact *= i

print (n, runsum, fact)


"""
# If you are interested: Dumb Ideas Below
 
# Eq. for Running sum: Sum = (n * (n + 1))/2
# runsum = (n * (n + 1))/2 
# runsum = 1 + 2 (1+1) + 3(2+1) ... n

runsum = n 
for i in range (1, n): 
	runsum += i

# Testing loop for Factorial, Eq. of Fac = n! = (n)(n-1)(n-1)...2*1
fac = n 
for i in range (1, n): 
	fac = fac * i

print (n, runsum, fac) 

# Other idea
number = n 
fac = 1
for i in range (1, number + 1):
	fac = fac * i 
	print (fac)
"""

"""
# expected output
python3 11sumfac.py
5 15 120
"""
