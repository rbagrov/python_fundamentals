import re

def punctuation_validator(text):

    sentences = re.split('[.!?]', text)

    for sentence in sentences:
        sentence.strip()

        # not working
        if sentence[0].isupper():
            print('ok')
        print('no')



punctuation_validator("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas in pulvinar augue, vel hendrerit nibh. Fusce mattis diam ut augue aliquet consequat. Etiam non commodo sapien. Curabitur a felis fringilla, pretium elit et, ornare justo.")