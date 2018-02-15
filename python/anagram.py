from collections import Counter

def anagrams(word, words):
    return list(filter(lambda element: Counter(word) == Counter(element), words))