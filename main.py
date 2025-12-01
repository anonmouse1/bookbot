import sys
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        countw = count_words(file_contents)
        sorted_chars = sort_char_counts(char_count(file_contents))
        print("============ BOOKBOT ============ \nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
        print(f"Found {countw} total words")
        print("--------- Character Count -------")
        for keyp in sorted_chars:
            print(keyp["char"] + ": " + str(keyp["num"]))
        print("============= END ===============")

from stats import count_words,char_count,sort_char_counts 

def main():
    #get_book_text("./books/frankenstein.txt")
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    elif len(sys.argv) > 1:
        get_book_text(sys.argv[1])
        sys.exit(0)

    
    
main()
