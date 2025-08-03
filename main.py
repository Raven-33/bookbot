def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    words = num_words(book_text)
    print (f"{words} words found in the document")

def num_words (book_text):
    word_l = book_text.split()
    words = len(word_l)
    return words
    
main()