#!/usr/bin/env python

"""mapper.py"""

import sys

top_words =["sport", "game", "team", "win", "get", "like", "one", "final", "just", "play"]

for line in sys.stdin : 
    words = line.split()
    for word in words :    
        for top_word in top_words:
            # for word in row :
            if top_word in words:
                if top_word != word: 
                    print ('%s\t%s' % ((top_word, word), 1))
