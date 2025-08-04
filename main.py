from stats import num_words
from stats import count_char
from stats import list_d

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    words = num_words(book_text)
    char = count_char(book_text)
    sort = []
    for i,e in char.items():
        sort.append({"char":i,"num":e})
    sort.sort(reverse=True,key=list_d)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for i in sort:
       character = i["char"]
       count = i["num"]
       if character.isalpha():
           print(f"{character}: {count}")

    print("============= END ===============")
  


main()