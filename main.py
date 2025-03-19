import sys
from stats import count_words, count_charachters, sort_char_count, print_report

def get_book_text(filepath):
    try:
        with open(filepath) as file:
            return file.read()
    except FileNotFoundError:
        return "Error: File not found. Please check the file path."
    except Exception as e:
        return f"An error occurred: {e}"
    

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    bookPath = sys.argv[1]
    bookText = get_book_text(bookPath)
    countWords = count_words(bookText)
    countChars = count_charachters(bookText)
    sortChar = sort_char_count(countChars)
    print_report(bookText, countWords, sortChar)


if __name__ == "__main__":
    main()
