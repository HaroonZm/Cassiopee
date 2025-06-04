def build_book_index():
    """
    Collects entries (word, page number) from the user and builds
    an index mapping each word to all its page numbers.

    Returns:
        dict: Dictionary where keys are words and values are lists of page numbers.
    """
    book_index = {}
    while True:
        try:
            # Prompt the user to enter a word and page number separated by space
            user_input = input()
            # Split the input into the word and the page number
            word, page = user_input.split(' ')
            # Convert the page number from string to integer
            page = int(page)
            # Retrieve the current list of pages for the word if it exists
            page_list = book_index.get(word)
            if page_list:
                # If the word already exists in the index, append the page number
                page_list.append(page)
            else:
                # Otherwise, create a new entry for the word with the page number
                book_index[word] = [page]
        except Exception:
            # If an error occurs (e.g. input can't be split, conversion fails, or EOFError),
            # break out of the loop (assume input has ended)
            break
    return book_index

def print_book_index(book_index):
    """
    Prints the book index in alphabetical order of words.
    For each word, prints the word and the list of its page numbers in ascending order.

    Args:
        book_index (dict): Dictionary with words as keys and list of page numbers as values.
    """
    # Iterate over the words in the index, sorted alphabetically
    for word in sorted(book_index.keys()):
        print(word)
        # Retrieve and sort the list of page numbers for the current word
        pages = sorted(book_index.get(word))
        # Join the page numbers as strings separated by spaces and print them
        print(' '.join(map(str, pages)))

def main():
    """
    Main execution function to build the book index from user input and print it.
    """
    # Collect entries from the user
    index = build_book_index()
    # Print the formatted index
    print_book_index(index)

# Entry point of the script
if __name__ == '__main__':
    main()