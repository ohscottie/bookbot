import sys
from stats import get_num_words, get_num_char

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]

    print("============ BOOKBOT ============")

    print(f"Analyzing book found at {file_path}...")
    book_text = get_book_text(file_path)
    
    num_words = get_num_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    num_char = get_num_char(book_text)
    print("--------- Character Count -------")
    for item in num_char:
        print(f"{item["char"]}: {item["num"]}")

    print("============= END ===============")

main()

