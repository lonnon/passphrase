#!/usr/bin/env python

# passphrase
#
# Generates a passphrase from random words (four by default, number may
# be specified as first argument on command line). By default, words are
# between 6 and 10 characters in length. Different minimum and maximum
# word lengths may be specified in the seconda and third command line
# arguments, respectively.

import random
import sys
import os
import glob
import re

try: length = int(sys.argv[1])
except IndexError: length = 4
try: minimum = int(sys.argv[2])
except IndexError: minimum = 6
try: maximum = int(sys.argv[3])
except IndexError: maximum = 10
if minimum > maximum:
    maximum = minimum

dictionaries = {int(re.search(r'[0-9]+$', f).group()):f for f in glob.glob('dictionary_letters_*')}
words = list()
for i in range(minimum, maximum + 1):
    with open(dictionaries[i], mode='r', encoding='utf-8') as dictionary:
        for line in dictionary:
            words.append(line.strip())

r = random.Random()
output = [r.choice(words) for n in range(length)]
print(' '.join(output))
print
