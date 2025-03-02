def main():
    import sys
    # Now you can use sys.argv
    print(sys.argv)  # This will show all command-line arguments
    path=sys.argv[1]
    book_text = get_book_text(path)
    from stats import get_num_words
    word_count = get_num_words(book_text)
    from stats import get_num_chars
    number_of_chars = get_num_chars(book_text)
    from stats import get_sorted
    sorted_chars = get_sorted(number_of_chars)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Directly use sorted_chars, filtering for alphabetic characters
    for char_dict in sorted_chars:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['count']}")
    
    print("============= END ===============")

#f.read is turning inputs into strings
def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

main()
