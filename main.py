import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

from stats import word_count

from stats import char_count

from stats import sort
def main():
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    wordcount = word_count(text)
    charcount = char_count(text)
    sorted = sort(charcount)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print("--------- Character Count -------")
    for char in sorted:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============") 
    
    
if __name__ == "__main__":
    main()





