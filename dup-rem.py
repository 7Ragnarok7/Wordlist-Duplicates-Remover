#!/usr/bin/env python3
from sys import argv
from time import sleep

try: file1, file2 = argv[1], argv[2]
except IndexError: exit(print("Usage: python dup-rem.py input-file output-file {Optional arguments: asc, dsc}" ))

print("\nRemoving duplicates........")

with open (file1, 'r') as file1, open (file2, 'w') as file2:
	old = file1.readlines()
	len1 = len(old)
	new = list(set(old))
	if "asc" in argv: new.sort()
	elif "dsc" in argv: new.sort(reverse=True)
	file2.writelines(new)
	
sleep(1)
print ("\nTotal number of lines in the input file:", len1)
print ("Total number of lines after removing duplicates:", len(new), end="\n\n")
