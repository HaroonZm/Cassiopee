def get_input():
    return raw_input()

def replace_mew(s):
    return s.replace('mew', '[1]')

def replace_me(s):
    return s.replace('me', 'm[1]e')

def replace_ew(s):
    return s.replace('ew', 'e[1]w')

def replace_m(s):
    return s.replace('m', '[')

def replace_e(s):
    return s.replace('e', ',')

def replace_w(s):
    return s.replace('w', ']')

def perform_replacements(s):
    s = replace_mew(s)
    s = replace_me(s)
    s = replace_ew(s)
    s = replace_m(s)
    s = replace_e(s)
    s = replace_w(s)
    return s

def collapse_pattern_once(s):
    return s.replace('[[1],[1]]', '[1]')

def collapse_pattern_n_times(s, n):
    for _ in range(n):
        s = collapse_pattern_once(s)
    return s

def is_cat(s):
    return s == '[1]' or s == ''

def print_result(is_cat_flag):
    if is_cat_flag:
        print 'Cat'
    else:
        print 'Rabbit'

def main():
    s = get_input()
    s = perform_replacements(s)
    s = collapse_pattern_n_times(s, 500)
    result = is_cat(s)
    print_result(result)

main()