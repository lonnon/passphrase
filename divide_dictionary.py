#!/usr/bin/env python

# divide_dictionary
#
# Splits dictionary file into multiple files based on number of letters
# per word. Dictionary file may be specified as the first argument on
# the command line; default is "non_proper_dictionary".

import sys

try: dictionary = int(sys.argv[1])
except IndexError: dictionary = 'non_proper_dictionary'

numbers = set()
with open(dictionary, mode='r', encoding='utf-8') as input:
    for line in input:
        numbers.add(len(line.strip()))

    filenames = {f:'dictionary_letters_{0}'.format(f) for f in numbers}
    files = {number:open(filename, mode='w', encoding='utf-8') for number, filename in filenames.items()}

    input.seek(0)
    for line in input:
        word = line.strip()
        files[len(word)].write(line)
    for f in files.values():
        f.close()
