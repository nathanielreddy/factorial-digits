#!/usr/bin/python3
# -----------------------------------------------------------
# Solves numerical algorithmic problem for factorial digits
# factorial-digits
# Version: 1.0
# GNU Public License (GPL)
# -----------------------------------------------------------

#import libraries
import argparse
import numpy

#create n! parser
parser = argparse.ArgumentParser(description='Calculate sum of n! factorial.')
parser.add_argument('n', type=int, help='Provide a integer to find factorial digits.')
args = parser.parse_args()

#solution


#output to check
print(numpy.math.factorial(args.n))