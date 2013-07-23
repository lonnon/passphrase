#!/usr/bin/env python

import random
import sys

try: length = int(sys.argv[1])
except IndexError: length = 4

r = random.Random()
words = [ x.strip() for x in open('/usr/share/dict/words', 'r').readlines() ]
for x in xrange(length):
    print r.choice(words),
print
