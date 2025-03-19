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