def read_input_line():
    return input()

def parse_line(line):
    return line.split(' ')

def convert_to_int(s):
    return int(s)

def get_word_and_page():
    line = read_input_line()
    word, page_str = parse_line(line)
    page = convert_to_int(page_str)
    return word, page

def get_page_list(book_index, word):
    return book_index.get(word)

def append_page(page_list, page):
    page_list.append(page)

def add_new_page_list(book_index, word, page):
    book_index[word] = [page]

def process_word_page(book_index, word, page):
    page_list = get_page_list(book_index, word)
    if page_list:
        append_page(page_list, page)
    else:
        add_new_page_list(book_index, word, page)

def read_input(book_index):
    while True:
        try:
            word, page = get_word_and_page()
            process_word_page(book_index, word, page)
        except Exception:
            break

def get_sorted_keys(book_index):
    return sorted(book_index.keys())

def get_sorted_pages(book_index, word):
    return sorted(book_index.get(word))

def format_pages(pages):
    return ' '.join(map(str, pages))

def print_word(word):
    print(word)

def print_pages(pages_str):
    print(pages_str)

def print_index(book_index):
    for word in get_sorted_keys(book_index):
        print_word(word)
        pages = get_sorted_pages(book_index, word)
        pages_str = format_pages(pages)
        print_pages(pages_str)

def main():
    book_index = {}
    read_input(book_index)
    print_index(book_index)

main()