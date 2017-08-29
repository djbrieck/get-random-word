#This file open a list of words one per line, and writes to standard out a valid output for a javascript varabile dictionary_english

import re
file = open('words_alpha.txt','r')

print "var dictionary_english = [\"PLACEHOLDER_NO_RANDOM_ZERO\",",
for line in file:
    print "\"" + re.sub("\W", "", line)+ "\",",

print "];",
