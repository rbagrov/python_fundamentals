# This file contains a method for inserting words in a text
import random

def insert(word, index, text):
    """ This function insert a given word in a given text at a given position """
    try:
        if index < 0:
            raise IndexError

        output = text[:index] + word + text[index:]
    except TypeError:
        print('inserted word must be string')
        return
    except IndexError:
        print('index must be greater than -1')
        return

    return output
