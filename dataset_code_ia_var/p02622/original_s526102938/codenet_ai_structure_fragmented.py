def read_input():
    return input()

def to_lower(s):
    return s.lower()

def to_list(s):
    return list(s)

def get_first_string():
    return read_input()

def get_second_string():
    return read_input()

def prepare_string(s):
    lower_s = to_lower(s)
    return to_list(lower_s)

def get_strings():
    s1 = get_first_string()
    s2 = get_second_string()
    return prepare_string(s1), prepare_string(s2)

def strings_length(s):
    return len(s)

def index_range(length):
    return range(0, length)

def get_char_at(s, i):
    return s[i]

def chars_differ(c1, c2):
    return c1 != c2

def count_differences(S, T):
    res = 0
    for i in index_range(strings_length(S)):
        c1 = get_char_at(S, i)
        c2 = get_char_at(T, i)
        if chars_differ(c1, c2):
            res = increment(res)
    return res

def increment(x):
    return x + 1

def output_result(result):
    print(result)

def main():
    S, T = get_strings()
    differences = count_differences(S, T)
    output_result(differences)

main()