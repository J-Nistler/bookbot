def count_words (corpus):
    word_count = 0
    word_count = len(corpus.split())
    return word_count

def count_letters (corpus):
    letter_list = [char.lower() for char in corpus]
    char_dict = {}

    for char in letter_list:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def sort_results (char_dict):
    sorted_list = []

    for key in char_dict:
        if key.isalpha():
            new_dict = {}
            new_dict["char"] = key
            new_dict["num"] = char_dict.get(key)
            sorted_list.append(new_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list