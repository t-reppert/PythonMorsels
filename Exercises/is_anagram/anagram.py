import string
import unicodedata


def is_anagram(string1, string2):

    s1 = unicodedata.normalize('NFKD', string1).encode('ASCII', 'ignore').decode('utf-8')
    s2 = unicodedata.normalize('NFKD', string2).encode('ASCII', 'ignore').decode('utf-8')
    string1 = sorted(s1.lower().replace(' ', '').translate(str.maketrans('', '', string.punctuation)))
    string2 = sorted(s2.lower().replace(' ', '').translate(str.maketrans('', '', string.punctuation)))

    if string1 == string2:
        return True
    else:
        return False
