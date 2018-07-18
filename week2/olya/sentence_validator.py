import re

def sentence_validator(text):
    """
    Check  if all sentences in the text are valid
        Args: string
        Returns: true or false
    """

    pattern = "[.?!]"
    sentences = re.split(pattern, text)

    for sentence in sentences[:-1]:
        word = sentence.strip()
        if word[0].islower():
            return False
    for sentence in sentences[:-1]:
        comma_pattern = ",(?=\S)|:"
        commas = re.split(comma_pattern, sentence)
        if commas.__len__() != 1:
            return False
    return True


test_text = "Sed placerat ligula libero! Donec eu blandit mi. Sed sed nisi ipsum. Donec facilisis sagittis enim, a dignissim augue gravida at. Nullam quis diam scelerisque, sodales ante ac, condimentum nibh? "
a = sentence_validator(test_text)
print(a)


