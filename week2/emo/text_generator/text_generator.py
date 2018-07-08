# This file contains a random text generator function

import string
import random

def text_generator(size=1000, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits + ' ,!.'):
    """ This method generates a random text with default lenght of 1000 and all ascii chars and digits and space """
    return ''.join(random.choice(chars) for x in range(size))
