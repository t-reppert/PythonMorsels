from collections import Counter
import re


def count_words(words):
    words_list = re.findall('[a-zA-Z\']+', words)
    return Counter([word.lower() for word in words_list])
