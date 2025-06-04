def get_input():
    return input()

def string_to_list(S):
    return list(S)

def get_length(s):
    return len(s)

def initialize_ans():
    return 0

def initialize_black_index():
    return 0

def is_black(char):
    return char == 'B'

def increase_black_index(black_index):
    return black_index + 1

def should_continue(s, i):
    return is_black(s[i])

def should_swap(s, i):
    return is_black(s[i-1])

def calculate_increment(l_s, i, black_index):
    return l_s - i - black_index

def set_black(s, i):
    s[i] = 'B'

def set_white(s, i):
    s[i] = 'W'

def print_result(ans):
    print(ans)

def process_string():
    S = get_input()
    s = string_to_list(S)
    l_s = get_length(s)
    ans = initialize_ans()
    black_index = initialize_black_index()
    for i in reversed(range(1, l_s)):
        if should_continue(s, i):
            black_index = increase_black_index(black_index)
            continue
        if should_swap(s, i):
            ans += calculate_increment(l_s, i, black_index)
            set_black(s, i)
            set_white(s, i-1)
            black_index = increase_black_index(black_index)
    print_result(ans)

process_string()