def get_input():
    try:
        return input().split()
    except EOFError:
        return None

def parse_input_line(line):
    if line is None:
        return None, None
    if len(line) != 2:
        return None, None
    return line[0], line[1]

def key_exists(key, key_list):
    return key in key_list

def index_of_key(key, key_list):
    return key_list.index(key)

def append_page_to_existing_key(key, page, key_list, page_list):
    idx = index_of_key(key, key_list)
    page_list[idx].append(int(page))

def add_new_key_and_page(key, page, key_list, page_list):
    key_list.append(key)
    page_list.append([int(page)])

def process_input(key_list, page_list):
    while True:
        line = get_input()
        key, page = parse_input_line(line)
        if key is None:
            break
        if key_exists(key, key_list):
            append_page_to_existing_key(key, page, key_list, page_list)
        else:
            add_new_key_and_page(key, page, key_list, page_list)

def copy_key_list(key_list):
    return key_list[:]

def sort_key_list(key_list):
    key_list.sort()

def print_key_and_pages(key, key_list, page_list):
    print(key)
    pages = page_list[index_of_key(key, key_list)][:]
    pages.sort()
    print(' '.join(map(str, pages)))

def main():
    key_list = []
    page_list = []
    process_input(key_list, page_list)
    sorted_keys = copy_key_list(key_list)
    sort_key_list(sorted_keys)
    for key in sorted_keys:
        print_key_and_pages(key, key_list, page_list)

main()