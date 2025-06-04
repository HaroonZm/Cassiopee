import itertools

def read_input():
    return input()

def split_input(s):
    return s.split()

def map_to_int(lst):
    return list(map(int, lst))

def get_sum(lst):
    return sum(lst)

def get_combinations(lst, r):
    return itertools.combinations(lst, r)

def compute_abs_difference(total, comb):
    return abs(total - 2 * sum(comb))

def append_to_list(lst, val):
    lst.append(val)

def find_min(lst):
    return min(lst)

def main():
    s = read_input()
    splitted = split_input(s)
    a = map_to_int(splitted)
    b = get_sum(a)
    comb = get_combinations(a, 2)
    sa = []
    for i in comb:
        diff = compute_abs_difference(b, i)
        append_to_list(sa, diff)
    print(find_min(sa))

main()