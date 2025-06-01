import sys
import itertools

def read_input():
    f = sys.stdin
    return f

def read_two_lines(f):
    return [list(map(int, f.readline().split())) for _ in range(2)]

def unpack_first_elements(lists):
    return [lst[0] for lst in lists]

def get_n_and_m(nhm, mkg):
    n = nhm[0]
    m = mkg[0]
    return n, m

def pair_lists(nhm, mkg):
    goto_iimoriyama = list(zip(*[nhm]*2))
    goto_turugajyo = list(zip(*[mkg]*2))
    return goto_iimoriyama, goto_turugajyo

def merge_pairs(goto_iimoriyama, goto_turugajyo):
    combined = goto_iimoriyama + goto_turugajyo
    unique_combined = list(set(combined))
    return unique_combined

def sort_pairs(pairs):
    return sorted(pairs)

def format_time_pairs(pairs):
    formatted = []
    for h, m in pairs:
        formatted.append('{}:{:02d}'.format(h, m))
    return formatted

def print_times(times):
    print(*times)

def main():
    f = read_input()
    nhm, mkg = read_two_lines(f)
    n, m = get_n_and_m(nhm, mkg)
    goto_iimoriyama, goto_turugajyo = pair_lists(nhm, mkg)
    combined = merge_pairs(goto_iimoriyama, goto_turugajyo)
    sorted_pairs = sort_pairs(combined)
    formatted_times = format_time_pairs(sorted_pairs)
    print_times(formatted_times)

main()