import re

def read_input():
    return input()

def assign_initial_values():
    s = read_input()
    return (s, s)

def pattern():
    return r'(m|e)mew(e|w)'

def replace_pattern(s, pat):
    return re.sub(pat, r'\1\2', s)

def is_equal(a, b):
    return a == b

def process_string(b, s):
    pat = pattern()
    prev = b
    curr = s
    while True:
        curr = replace_pattern(curr, pat)
        if is_equal(prev, curr):
            break
        prev = curr
    return curr

def result_idx(processed):
    return processed == 'mew'

def result_label(idx):
    return ['Rabbit', 'Cat'][idx]

def main():
    b, s = assign_initial_values()
    processed = process_string(b, s)
    idx = result_idx(processed)
    label = result_label(idx)
    print(label)

main()