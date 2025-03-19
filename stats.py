def count_words(text):
    return len(text.split())

def count_charachters(text):
    char_counts = {}
    for char in text:
        lowercase_char = char.lower()

        if lowercase_char in char_counts:
            char_counts[lowercase_char] += 1
        else:
            char_counts[lowercase_char] = 1

    return char_counts

def sort_char_count(char_count):
    result = []
    for char, count in char_count.items():
        char_dict = {"char": char, "count": count}
        result.append(char_dict)
    
    def sort_on(dict):
        return dict["count"]
    
    result.sort(reverse=True, key=sort_on)
    return result

def print_report(path, word_count, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")