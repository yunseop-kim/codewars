def my_alphabet_position(text):
    return ' '.join([str(ord(char) - 96) for char in filter(lambda x: x.isalpha(), text.replace(' ', '').lower())])

# best
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

# 람다를 내가 너무 좋아하는거 같다. 파이썬은 더 쉽구나.