def get_num_words(book_text):
    word_count = 0
    book_text_list = book_text.split()
    for word in book_text_list:
        word_count += 1
    return word_count

def get_num_chars(book_text):
    num_chars = {}
    book_text_low = book_text.lower()
    for char in book_text_low:
        if char in num_chars:
            num_chars[char] += 1
        else:
            num_chars[char] = 1
    return num_chars

def get_sorted(char_counts):
    # Create a list of dictionaries
    chars_list = []
    for char, count in char_counts.items():
        chars_list.append({"char": char, "count": count})
    
    # Define the sort_on function
    def sort_on(dict):
        return dict["count"]
    
    # Sort the list
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list
