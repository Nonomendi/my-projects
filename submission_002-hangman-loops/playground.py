import random
def fill_in_char(original_word, answer_word, char):
    word_chars = [i for i in original_word]
    undone_chars = [i for i in answer_word]
    if char in word_chars and char not in undone_chars:
        undone_chars[word_chars.index(char)] = char
    return "".join(undone_chars)


print(fill_in_char("mendi", "__n__", "m"))