from stats import get_num_words, get_num_chars
import sys

def get_book_text():
    with open(sys.argv[1]) as f:
        return f.read()

def print_report(word_count, sorted_chars):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")  

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)     
    word_count = get_num_words(get_book_text())
    sorted_chars = get_num_chars(get_book_text())
    print_report(word_count,sorted_chars)
    

if __name__ == "__main__":
    main()