from stats import num_words
from stats import count_char

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    words = num_words(book_text)
    char = count_char(book_text)
    print (f"{words} words found in the document")
    print(char)


main()