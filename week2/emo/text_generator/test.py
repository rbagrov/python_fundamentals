# This is a test file to show hoe the text generator and insert functions work

import random

from text_generator import text_generator
from insert_words import insert

text = text_generator()
words = [' TEST ']* 100

for word in words:
    text = insert(word, random.randint(0, len(text)), text)

print(text)
