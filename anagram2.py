#!/usr/bin/env python


def anagram(word1, word2):

    return sorted(word1.lower()) == sorted(word2.lower())

print("Are these words anagrams of each other?")
while True:
	input1 = raw_input("Please enter the first word: ")
	input2 = raw_input("Please enter the second word: ")
	if input1.isalpha() and input2.isalpha():
		if anagram(input1, input2):
			print("Yes, %s and %s are anagrams of each other" % (input1, input2))
		else:
			print("No, %s and %s are not anagrams of each other" % (input1, input2))
	else:
		print("Please enter a word containing only letters")
	again = raw_input("Do you want to quit? y/n --> ")
	if again == "y":
		break
