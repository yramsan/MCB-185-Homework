#!/usr/bin/env python3
# 61dust.py

import argparse

# Write a program that finds and masks low entropy sequence
# Use argparse for the following parameters
#   sequence file
#   window size
#   entropy threshold
#   lowercase or N-based masking
# The program should output a FASTA file (but with Ns or lowercase)
# Use argparse
# Use the mcb185.read_fasta() function
# Put more functions in your mcb185.py library

parser = argparse.ArgumentParser(description='Outputs sequence in FASTA format with low entropy regions masked')

parser.add_argument('--fasta', required=True, type=str,
	metavar='<str>', help='requires a string')
parser.add_argument('--wdsz', required=True, type=int,
	metavar='<int>', help='requires an integer to specify window size')
parser.add_argument('--eth', required=True, type=float,
	metavar='<float>', help='requires a floating point to set entropy threshold')
parser.add_argument('--lowercase', action='store_true', help='lowercase or N-based masking. N-based default')

arg = parser.parse_args()

for name, seq in mcb185.read_fasta(arg.fasta):
    seq = seq.upper()
    output = ""
    for i in range(0, len(seq) - arg.wdsz + 1): 
		window = seq[i:i+arg.wdsz]
		deltaS = mcb185.entropycalc(window)
		if deltaS < arg.eth:
            if arg.lowercase: 
                output += "N"
            else: 
                output += seq[i].lower()
        else: 
            output += seq[i]
    for i in range(len(seq) - arg.wdsz + 1, len(seq)): 
        output += seq[i]
    print(name, output)
    

