#!/usr/bin/env python


def anagram(word1, word2):

    return sorted(word1.lower()) == sorted(word2.lower())

