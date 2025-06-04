def get_input():
    return input().split()

def parse_ints(items):
    return list(map(int, items))

def get_n_t():
    return parse_ints(get_input())

def get_t():
    return parse_ints(get_input())

def iterate_pairs(lst):
    return zip(lst, lst[1:])

def time_diff(prev, curr):
    return curr - prev

def min_time(diff, T):
    return min(diff, T)

def update_output(o, val):
    return o + val

def process_times(t, T):
    o = T
    pairs = iterate_pairs(t)
    for i, j in pairs:
        diff = time_diff(i, j)
        minval = min_time(diff, T)
        o = update_output(o, minval)
    return o

def main():
    n, T = get_n_t()
    t = get_t()
    result = process_times(t, T)
    print(result)

main()