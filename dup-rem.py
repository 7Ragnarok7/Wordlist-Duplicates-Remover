#!/usr/bin/env python3
from sys import argv
from time import sleep

try: file1, file2 = argv[1], argv[2]
except IndexError: exit(print("Usage: python dup-rem.py input-file output-file"))

set1 = set()
count = 0
print("\nRemoving duplicates........")

with open (file1, 'r') as file1, open (file2, 'w') as file2:
	for line in file1:
		count += 1
		set1.add(line)
	for line in set1: file2.write(line)
sleep(1)
print ("\nTotal number of lines in the input file:", count)
print ("Total number of lines after removing duplicates:", len(set1), end="\n\n")
