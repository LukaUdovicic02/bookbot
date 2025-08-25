from stats import get_num_words, get_num_chars

def get_book_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents


def main():
    #get_num_words(get_book_text())
    get_num_chars(get_book_text())
main()