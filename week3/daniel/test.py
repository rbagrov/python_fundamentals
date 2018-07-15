import string
import random
from rot_codec import ROTEncoderDecoder

class Verifier(object):

    def generate_text(self, size = 5, chars = string.ascii_uppercase + string.ascii_lowercase):
        if size < 1:
            return ''
        return ''.join(random.choice(chars) for x in range(size))

    def verify(self):
        codec = ROTEncoderDecoder()
        txt = self.generate_text(size = 6)
        encoded_txt = codec.rot_encode_decode(2, txt)
        decoded_txt = codec.rot_encode_decode(2, encoded_txt, False)

        if txt != decoded_txt:
            print('Not working')
        else:
            print('Working fine')


verifier = Verifier()
verifier.verify()