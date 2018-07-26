import string


class ROTEncoderDecoder(object):

    def calculate_encode_offset(self, index, offset):
        result = index + offset
        if result > 26:
            result = result - 26
        result -= 1

        return result

    def calculate_decode_offset(self, index, offset):
        result = index - offset
        if result <= 0:
            result = result + 26
        result -= 1

        return result

    def calculate_new_index(self, rot, index, encode):
        offset = rot % 26

        if encode:
            offset = self.calculate_encode_offset(index, offset)
        else:
            offset = self.calculate_decode_offset(index, offset)

        return offset

    def rot_encode_decode(self, rot=0, word='', encode=True):
        result = ''

        if len(word) < 1:
            print('No string provided')
            return None

        if rot < 1:
            print('Invalid ROT index')
            return None

        for i in range(len(word)):
            uppercase = True
            index = string.ascii_uppercase.find(word[i])

            if index < 0:
                uppercase = False
                index = string.ascii_lowercase.find(word[i])

            if index < 0:
                result += word[i]
                continue

            new_index = self.calculate_new_index(rot, index+1, encode)
            if uppercase:
                result += string.ascii_uppercase[new_index]
            else:
                result += string.ascii_lowercase[new_index]

        print('Input String: {}'.format(word))
        print('ROT Index: {}'.format(rot))
        print('ROT Encoded/Decoded String: {} \n'.format(result))

        return result
