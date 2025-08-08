def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_char(text):
    num_char = {}
    for char in text:
        c = char.lower()
        if c in num_char:
            num_char[c] += 1
        else:
            num_char[c] = 1
    return num_char
