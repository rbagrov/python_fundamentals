class ROTEncoderDecoder:
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    alphabet_lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


    def calculateNewIndex(self, rot, index, encode):
        offset = rot % 26

        if encode:
            if index + offset > 26:
                offset = index + offset - 26
            else:
                offset = index + offset
        else:
            if index - offset > 0:
                offset = index - offset
            else:
                offset = index - offset + 26


        return offset-1


    def rotEncoderDecoder(self, rot = 0, word = '', encode = True):
        result = ''

        if len(word) < 1:
            print('No string provided')
            return

        if rot < 1:
            print('Invalid ROT index')
            return

        for i in range(len(word)):
            index = -1
            uppercase = True

            if word[i] in alphabet:
                index = alphabet.index(word[i])
            elif word[i] in alphabet_lowercase:
                uppercase = False 
                index = alphabet_lowercase.index(word[i])
            else:
                break

            if uppercase:
                result = result + alphabet[calculateNewIndex(rot, index+1, encode)]
            else:
                result = result + alphabet_lowercase[calculateNewIndex(rot, index+1, encode)]

        print('Input String: {}'.format(word))
        print('ROT Index: {}'.format(rot))
        print('ROT Encoded/Decoded String: {}'.format(result))