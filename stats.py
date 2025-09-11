def count_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def count_letters(text):
    lower_case_text = text.lower()
    letter_count = {}
    for e in lower_case_text:
        if e in letter_count:
            letter_count[e] = letter_count[e] + 1
        else:
            letter_count[e] = 1
    return letter_count

def sort_on(items):
    return items["num"]

def dict_into_list_of_dicts(dict):
    list_of_dict = []
    for e in dict:
        temp_dict = {}
        temp_dict["char"] = e
        temp_dict["num"] = dict[e]
        list_of_dict.append(temp_dict)
    
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict