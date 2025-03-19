from stats import count_words, count_charachters

def get_book_text(filepath):
    try:
        with open(filepath) as file:
            return file.read()
    except FileNotFoundError:
        return "Error: File not found. Please check the file path."
    except Exception as e:
        return f"An error occurred: {e}"
    
def count_words(text):
    return len(text.split())


def main():
    book_text = get_book_text("books/frankenstein.txt")
    count_chars = count_charachters(book_text)
    print(f"{count_words(book_text)} words found in the document")
    print(count_chars)

if __name__ == "__main__":
    main()
