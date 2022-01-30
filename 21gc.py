#!/usr/bin/env python3

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
# Use all three formatting methods
# Credit to my new friend Hongtao for helping with this code!

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT' # feel free to change

gc= 0 
for i in range(len(dna)): 
	if dna[i] =='C' or dna[i] =='G':
		gc += 1 
		
frac = (gc)/(len(dna))
		
print (f'{frac:.2f}')
print('{:.2f}' .format(frac))
print('%.2f' % (frac))


"""
python3 21gc.py
0.42
0.42
0.42
"""
