import re


def text_stats(text):
    '''Receives random text and returns statistics about it.'''
    capital_letters = len(re.findall('([A-Z][a-z]+)', text))
    words_count = len(re.findall('(\w+)', text))
    sentences_count = len(re.findall('([A-Z][^\.!?]*[\.!?])', text))
    occurences_of_and = len(re.findall(r'\band\b', text))

    return capital_letters, words_count, sentences_count, occurences_of_and
