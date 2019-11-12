#!/usr/bin/env python
#cc
"""mapper.py"""

import sys

top_words =["sport", "team", "soccer", "pm", "news", "us", "game", "footbal", "new", "home"]

for line in sys.stdin : 
    words = line.split()
    for word in words :    
        for top_word in top_words:
            # for word in row :
            if top_word in words:
                if top_word != word: 
                    print ('%s\t%s' % ((top_word, word), 1))
