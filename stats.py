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

    char_list = []
    for char, num in num_char.items():
        char_list.append({"char": char, "num": num})

    char_list.sort(reverse=True, key=sort_on)
    return char_list

def sort_on(items):
    return items["num"]
