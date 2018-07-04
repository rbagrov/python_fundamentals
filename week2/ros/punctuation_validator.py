import re

def punctuation_validator(text):

    sentences = re.split('[.!?]', text)

    for sentence in sentences:
        sentence.strip()

        # not working
        print(sentence[0])
        if sentence[0].isupper():
            return True
        return False



punctuation_validator("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas in pulvinar augue, vel hendrerit nibh. Fusce mattis diam ut augue aliquet consequat. Etiam non commodo sapien. Curabitur a felis fringilla, pretium elit et, ornare justo.")
