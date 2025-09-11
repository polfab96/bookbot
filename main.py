from stats import count_words
from stats import count_letters
from stats import dict_into_list_of_dicts

import sys

def main():
    try:
        book_path = sys.argv[1]
    except Exception as e:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)   

    text = get_book_text(book_path)
    num_words = count_words(text)

    num_letters = count_letters(text)

    sorted_list = dict_into_list_of_dicts(num_letters)
    print_report(book_path , num_words , sorted_list)

def get_book_text(path):
    with open(path) as f:
        text_as_string = f.read()
    return text_as_string

def print_report(book , num_words, sorted_list):
        
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for e in sorted_list:
        if e["char"].isalpha():
            print(f"{e["char"]}: {e["num"]}")
    print("============= END ===============")



main()