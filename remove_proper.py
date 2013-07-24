#!/usr/bin/env python

# remove_proper
#
# Removes proper nouns from dictionary file and writes out a new one.
# Dictionary file may be specified as the first command line argument;
# default is /usr/share/dict/words.

import sys

try: dictionary = int(sys.argv[1])
except IndexError: dictionary = '/usr/share/dict/words'

words = [ x for x in open(dictionary, 'r').readlines() if x.islower() ]

with open('non_proper_dictionary', mode='w', encoding='utf-8') as output:
    output.write(''.join(words))
