def read_input():
    return int(input()), list(map(int, input().split())), list(map(int, input().split()))

def sort_list(lst):
    return sorted(lst)

def convert_to_tuple(lst):
    return tuple(lst)

def generate_permutations(lst):
    from itertools import permutations
    return list(permutations(lst))

def find_index_in_permutations(perms, target):
    return perms.index(target)

def compute_absolute_difference(a, b):
    return abs(a - b)

def process_input(N, p, q):
    sorted_p = sort_list(p)
    sorted_q = sort_list(q)
    perms_p = generate_permutations(sorted_p)
    perms_q = generate_permutations(sorted_q)
    tuple_p = convert_to_tuple(p)
    tuple_q = convert_to_tuple(q)
    index_p = find_index_in_permutations(perms_p, tuple_p)
    index_q = find_index_in_permutations(perms_q, tuple_q)
    return compute_absolute_difference(index_p, index_q)

def main():
    N, p, q = read_input()
    result = process_input(N, p, q)
    print(result)

main()