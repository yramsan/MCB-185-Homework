
#!/usr/bin/env python3

import random
#random.seed(1) # comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence
# Credit goes to Hongtiao and Jan for helping me with this code! 


bp = 30 
dna = ''
atc = 0 
for i in range(bp):
	r=random.random()
	if r < 0.3: 
		atc += 1
		dna += 'A'
	elif r < 0.6:
		atc += 1
		dna += 'T'
	elif r < 0.8: 
		dna += 'C'
	else:
		dna +='G'
print(bp, atc/bp, dna)



"""
python3 22atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
