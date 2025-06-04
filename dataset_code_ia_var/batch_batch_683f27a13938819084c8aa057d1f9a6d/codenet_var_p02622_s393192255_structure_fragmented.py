def read_input():
    return input()

def get_string_1():
    return read_input()

def get_string_2():
    return read_input()

def get_length(s):
    return len(s)

def characters_differ(c1, c2):
    return c1 != c2

def count_differences(s, t):
    total = 0
    length = get_length(s)
    for idx in generate_indices(length):
        if check_difference(s, t, idx):
            total = increment(total)
    return total

def generate_indices(length):
    return range(length)

def check_difference(s, t, idx):
    return characters_differ(s[idx], t[idx])

def increment(val):
    return val + 1

def output_result(ans):
    print(ans)

def main():
    s = get_string_1()
    t = get_string_2()
    ans = count_differences(s, t)
    output_result(ans)

main()