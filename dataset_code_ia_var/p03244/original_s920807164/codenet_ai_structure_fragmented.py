from collections import Counter

def read_input():
    return int(input()), list(map(int, input().split()))

def extract_even_positions(v, n):
    return v[0:n:2]

def extract_odd_positions(v, n):
    return v[1:n:2]

def count_elements(lst):
    return Counter(lst)

def get_most_common(counter):
    return counter.most_common()

def get_first_element(c):
    return c[0][0]

def get_first_count(c):
    return c[0][1]

def get_second_count(c):
    return c[1][1] if len(c) > 1 else 0

def are_both_lengths_one(c1, c2):
    return len(c1) == 1 and len(c2) == 1

def is_length_one(c):
    return len(c) == 1

def calculate_output_different_elements(n, c1, c2):
    return n - get_first_count(c1) - get_first_count(c2)

def calculate_output_both_lengths_one(n):
    return n // 2

def calculate_output_c1_one(n, c1, c2):
    return n - get_first_count(c1) - get_second_count(c2)

def calculate_output_c2_one(n, c1, c2):
    return n - get_second_count(c1) - get_first_count(c2)

def calculate_output_both_more_than_one(n, c1, c2):
    return n - max(get_second_count(c1) + get_first_count(c2),
                   get_first_count(c1) + get_second_count(c2))

def main():
    n, v = read_input()
    v1 = extract_even_positions(v, n)
    v2 = extract_odd_positions(v, n)
    cc1 = count_elements(v1)
    cc2 = count_elements(v2)
    c1 = get_most_common(cc1)
    c2 = get_most_common(cc2)

    if get_first_element(c1) != get_first_element(c2):
        print(calculate_output_different_elements(n, c1, c2))
    else:
        if are_both_lengths_one(c1, c2):
            print(calculate_output_both_lengths_one(n))
        elif is_length_one(c1) and not is_length_one(c2):
            print(calculate_output_c1_one(n, c1, c2))
        elif is_length_one(c2) and not is_length_one(c1):
            print(calculate_output_c2_one(n, c1, c2))
        else:
            print(calculate_output_both_more_than_one(n, c1, c2))

main()