def get_first_string():
    return input()

def get_second_string():
    return input()

def get_string_length(s):
    return len(s)

def get_char_from_string(s, i):
    return s[i]

def chars_are_different(c1, c2):
    return c1 != c2

def increment_counter(counter):
    return counter + 1

def compare_strings(s, t):
    counter = 0
    length = get_string_length(s)
    for i in get_range(length):
        c1 = get_char_from_string(s, i)
        c2 = get_char_from_string(t, i)
        if chars_are_different(c1, c2):
            counter = increment_counter(counter)
    return counter

def get_range(n):
    return range(n)

def print_result(counter):
    print(counter)

def main():
    s = get_first_string()
    t = get_second_string()
    counter = compare_strings(s, t)
    print_result(counter)

main()