def get_input():
    return input()

def split_input(s):
    return s.split()

def count_elements(lst):
    from collections import Counter
    return Counter(lst)

def get_most_common(c):
    return c.most_common(1)

def extract_first_element(t):
    return t[0]

def extract_key_from_tuple(t):
    return t[0]

def key_length(e):
    return len(e)

def sort_by_length(lst):
    return sorted(lst, key=key_length)

def get_last(lst):
    return lst[-1]

def print_results(most_common, longest):
    print(most_common, longest)

def main():
    user_input = get_input()
    splitted = split_input(user_input)
    counter = count_elements(splitted)
    most_common_list = get_most_common(counter)
    most_common_tuple = extract_first_element(most_common_list)
    most_common_word = extract_key_from_tuple(most_common_tuple)
    sorted_by_len = sort_by_length(splitted)
    longest_word = get_last(sorted_by_len)
    print_results(most_common_word, longest_word)

main()