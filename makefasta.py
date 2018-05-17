#!/usr/bin/env python3

from random import choice

def DNAfasta(number, length):
    for num in range(number):
        print(">ID" + str(num) + choice("1258397") * 9)
        DNA = ""
        for numb in range(length):
            DNA += choice("AGTC")
        print(DNA)

DNAfasta(5, 10)