passphrase
==========

Python passphrase generator

This tool is inspired by Randall Munroe's xkcd comic ["Password Strength"](http://xkcd.com/936/). It generates random multi-word passphrases from dictionary words, resulting in a passphrase that's easier for humans to remember, but harder for machines to guess.

Usage:

    passphrase.py [words] [min] [max]

      words - Number of words in the passphrase. Default is 4.

      min - Minimum length of each word in the passphrase. Default is 6.

      max - Maximum length of each word in the passphrase. Default is 10.

The word lists were built from `/usr/share/dict/words` on Mac OS X 10.6.8. As word lists go, it contains an astonishing number of bizarre terms that may or may not actually qualify as English words, and probably serves to defeat the "easily remembered by humans" property possessed by a good passphrase. There are better lists of common words available; [Kevin's Word List Page](http://wordlist.sourceforge.net/) is a great place to look for better options.

The `remove_proper.py` script removes proper nouns from a word list, and `divide_dictionary.py` splits the list into smaller word lists based on the number of letters in each word.

This has also been done better, with tests, more options, and a nicer interface, by [smarter people than I](https://github.com/redacted/XKCD-password-generator).
