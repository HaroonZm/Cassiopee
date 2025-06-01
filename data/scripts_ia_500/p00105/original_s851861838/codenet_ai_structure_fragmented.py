import sys

def read_input_lines():
    return sys.stdin.readlines()

def strip_line(line):
    return line.strip()

def split_line(line):
    parts = line.split()
    word = parts[0]
    num = parts[1]
    return word, num

def dict_has_key(dictionary, key):
    return key in dictionary

def create_list():
    return list()

def append_to_list(lst, value):
    lst.append(value)

def convert_to_int(value):
    return int(value)

def get_dict_keys(dictionary):
    return dictionary.keys()

def sort_keys(keys):
    return sorted(keys)

def sort_list(lst):
    return sorted(lst)

def convert_to_str(value):
    return str(value)

def join_strings(strings, sep=" "):
    return sep.join(strings)

def print_value(value):
    print(value)

def process_input(dictionary):
    lines = read_input_lines()
    for line in lines:
        line = strip_line(line)
        word, num = split_line(line)
        if not dict_has_key(dictionary, word):
            dictionary[word] = create_list()
        append_to_list(dictionary[word], convert_to_int(num))

def process_output(dictionary):
    keys = get_dict_keys(dictionary)
    sorted_keys = sort_keys(keys)
    for key in sorted_keys:
        print_value(key)
        sorted_numbers = sort_list(dictionary[key])
        str_numbers = list(map(convert_to_str, sorted_numbers))
        joined = join_strings(str_numbers)
        print_value(joined)

def main():
    dictionary = dict()
    process_input(dictionary)
    process_output(dictionary)

main()