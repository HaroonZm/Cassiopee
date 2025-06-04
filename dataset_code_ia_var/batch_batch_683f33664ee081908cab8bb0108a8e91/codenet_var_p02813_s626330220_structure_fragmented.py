import itertools

def get_integer_input():
    return int(input())

def get_list_input():
    return list(map(int, input().split()))

def generate_range(n):
    return range(1, n+1)

def get_permutations(rng):
    return list(itertools.permutations(rng))

def permutation_to_list_tuple(perm):
    return [list(x) for x in perm]

def index_in_list(lst, item):
    return lst.index(item)

def abs_difference(a, b):
    return abs(a - b)

def main():
    n = get_integer_input()
    p_list = get_list_input()
    q_list = get_list_input()
    rng = generate_range(n)
    permutations_tuple = get_permutations(rng)
    combination_list = permutation_to_list_tuple(permutations_tuple)
    p_index = index_in_list(combination_list, p_list)
    q_index = index_in_list(combination_list, q_list)
    difference = abs_difference(p_index, q_index)
    print_result(difference)

def print_result(result):
    print(result)

main()