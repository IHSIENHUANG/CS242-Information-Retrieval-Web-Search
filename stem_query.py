import sys
import os
from nltk.stem import PorterStemmer  # stemming package for finding root words
import enchant  # all language dictionary package for checking existence of words
import re

stemmer = PorterStemmer()
unstemmed_list = sys.argv[1].split(" ")
for unstemmed_word in unstemmed_list:
	print(stemmer.stem(unstemmed_word)+" ")
