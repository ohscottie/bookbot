from stats import get_num_words, get_num_char

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    print("============ BOOKBOT ============")

    filepath = "books/frankenstein.txt"
    print(f"Analyzing book found at {filepath}...")
    book_text = get_book_text(filepath)
    
    num_words = get_num_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    num_char = get_num_char(book_text)
    print("--------- Character Count -------")
    for item in num_char:
        print(f"{item["char"]}: {item["num"]}")

    print("============= END ===============")

main()

