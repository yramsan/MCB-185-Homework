#!/usr/bin/env python3

# Write a program that prints out the position, frame, and letter of the DNA
# Try coding this with a single loop
# Try coding this with nested loops
# Credit to my new friend Hongtao for helping with this code!

dna = 'ATGGCCTTT' 

# Single Loop 
for i in range(len(dna)): 
	print(i, i % 3, dna[i])
print()	

# Nested Loop 
for i in range(0, len(dna)-2,3): 
	for j in range(3): 
		print(i+j, j, dna[i+j])


"""
python3 24frame.py
0 0 A
1 1 T
2 2 G
3 0 G
4 1 C
5 2 C
6 0 T
7 1 T
8 2 T
"""
