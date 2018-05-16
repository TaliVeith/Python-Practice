#!/usr/bin/env python3

from anagramfunc import anagram
import sys

# test if function returns expected answer
if anagram("lalala", "alalal") == False:
    print("Error! False negative!", file = sys.stderr)

if anagram("lalala", "allllalal") == True:
    print("Error! False positive!", file = sys.stderr)

# test if capital letters ignored
if anagram("Lalala", "lalala") == False:
    print("Error! Upper and lower letters not recognized as same!", file = sys.stderr)
