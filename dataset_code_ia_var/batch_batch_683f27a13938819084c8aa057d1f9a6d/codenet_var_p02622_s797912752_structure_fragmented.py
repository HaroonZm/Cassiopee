def get_input():
    return input()

def get_s():
    return get_input()

def get_t():
    return get_input()

def get_length(s):
    return len(s)

def get_char(s, i):
    return s[i]

def compare_chars(c1, c2):
    return c1 != c2

def increment(val):
    return val + 1

def init_sm():
    return 0

def print_result(res):
    print(res)

def process_diff(s, t):
    sm = init_sm()
    length = get_length(s)
    for i in range(length):
        c1 = get_char(s, i)
        c2 = get_char(t, i)
        if compare_chars(c1, c2):
            sm = increment(sm)
    return sm

def main():
    s = get_s()
    t = get_t()
    result = process_diff(s, t)
    print_result(result)

main()