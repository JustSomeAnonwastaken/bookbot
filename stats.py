def get_word_count(contents):
    print("----------- Word Count ----------")
    words = contents.split()
    count = len(words)
    print(f"Found {count} total words")

def get_letter_count(contents):
    print("--------- Character Count -------")
    letters_dict = {}
    for char in contents:
        letter = char.lower()
        if letter not in letters_dict:
            letters_dict[letter] = 1
        else:
            letters_dict[letter] += 1
    return letters_dict

def sort_on(items):
    return items["num"]

def sort_book_dict(dict):
    sort_list = []
    for key, value in dict.items():
        sort_list.append({"char": key, "num": value})
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list
    