def num_words (book_text):
    word_l = book_text.split()
    words = len(word_l)
    return words

def count_char (book_text):
    count = {}
    characters = book_text.lower()
    
    for i in characters:
        if i not in count:
            count[f"{i}"] = 0
        count[i] += 1
    return count
    
