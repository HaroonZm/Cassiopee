def read_input():
    s = input()
    k = int(input())
    return s, k

def init_vars(s):
    pre_c = ''
    count = 1
    first_char = s[0]
    last_char = s[-1]
    return pre_c, count, first_char, last_char

def group_counts(s):
    t = []
    pre_c, count, _, _ = init_vars(s)
    for c in s:
        count, pre_c, t = process_char(c, pre_c, count, t)
    finalize_group(count, t)
    return t

def process_char(c, pre_c, count, t):
    if c == pre_c:
        count += 1
    elif pre_c == '':
        pass
    else:
        t.append(count)
        count = 1
    pre_c = c
    return count, pre_c, t

def finalize_group(count, t):
    t.append(count)

def sum_half_groups(t):
    return sum(i // 2 for i in t)

def is_single_group(t):
    return len(t) == 1

def merge_ends_if_needed(t, s):
    first_char, last_char = s[0], s[-1]
    if first_char == last_char and not is_single_group(t):
        t[0] = t[0] + t[-1]
        t.pop(-1)
    return t

def solve():
    s, k = read_input()
    t = group_counts(s)
    count_1 = sum_half_groups(t)
    t2 = merge_ends_if_needed(list(t), s)
    count_2 = sum_half_groups(t2)
    if len(s) == 1:
        print(k // 2)
    elif is_single_group(t):
        print(k * len(s) // 2)
    else:
        print(count_1 + count_2 * (k - 1))

solve()