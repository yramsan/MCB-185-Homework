#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional
# Credit to my new friend Hongtao for helping with this code!

dna = 'ACTGAAAAAAAAAAA'
anti = '' 
for i in range (len(dna) -1, -1, -1):
	nt = dna[i]
	if nt == 'A': anti += 'T'
	elif nt == 'C': anti += 'G'
	elif nt == 'T': anti += 'A'
	elif nt == 'G': anti += 'C' 
	else: anti += 'O' 
print(anti) 

"""
python3 23anti.py
TTTTTTTTTTTCAGT
"""
