import re


def sentence_validator(text):
    """
    Checks if all sentences in the text are valid
        Args: string
        Returns: true or false
    """
    sentence_pattern = "[.?!]"
    comma_pattern = ",(?=\S)"
    sentences = re.split(sentence_pattern, text)

    for sentence in sentences:
        word = sentence.strip()
        if word != "":
            if word[0].islower():
                return False
            commas = re.split(comma_pattern, sentence)
            if len(commas) != 1:
                return False
        else:
            return True

    return True
