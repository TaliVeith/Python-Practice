#!/usr/bin/env python


def anagram(word1, word2):

	prime_num = {"a": 2, "c": 3, "b": 5, "e": 7, "d": 11, "g": 13, 
         "f": 17, "i": 19, "h": 23, "k": 29, "j": 31, "m": 37, 
         "l": 41, "o": 43, "n": 47, "q": 53, "p": 59, "s": 61, 
         "r": 67, "u": 71, "t": 73, "w": 79, "v": 83, "y": 89, 
         "x": 97, "z": 101}
	
	score1 = 1
	score2 = 1

	for let in word1:
		score1 *= prime_num[let.lower()]
	for let in word2:
		score2 *= prime_num[let.lower()]

	if score1 == score2:
		print("Yes, %s and %s are anagrams of each other" % (word1, word2))
	else:
		print("No, %s and %s are not anagrams of each other" % (word1, word2))


print("Are these words anagrams of each other?")
while True:
	input1 = raw_input("Please enter the first word: ")
	input2 = raw_input("Please enter the second word: ")
	if input1.isalpha() and input2.isalpha():
		anagram(input1, input2)
	else:
		print("Please enter a word containing only letters")
	again = raw_input("Do you want to quit? y/n --> ")
	if again == "y":
		break





