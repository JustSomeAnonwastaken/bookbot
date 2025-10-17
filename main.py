import sys
from stats import get_word_count
from stats import get_letter_count
from stats import sort_book_dict

def get_book_text(book):
    with open(book) as b:
        book_contents = b.read()
    return book_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    book = get_book_text(sys.argv[1])
    get_word_count(book)
    letter_count = get_letter_count(book)
    sorted_letters = sort_book_dict(letter_count)
    for item in sorted_letters:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")


main()