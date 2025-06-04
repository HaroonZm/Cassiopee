import itertools
import bisect

def generate_cube(n):
    return n ** 3

def generate_cubes_list(start, stop):
    return [generate_cube(n) for n in range(start, stop)]

def combination_pair_sum(pair):
    return pair[0] + pair[1]

def generate_num_list(cubes):
    pairs = itertools.combinations_with_replacement(cubes, 2)
    return [combination_pair_sum(pair) for pair in pairs]

def sort_list(lst):
    lst.sort()

def get_user_input():
    return int(input())

def calc_cube(n):
    return n ** 3

def bisect_index(sorted_list, value):
    return bisect.bisect(sorted_list, value)

def value_at_index_minus_one(lst, idx):
    return lst[idx - 1]

def calculate_difference(z_cube, num, idx):
    return z_cube - value_at_index_minus_one(num, idx)

def main_loop(num):
    while True:
        z = get_user_input()
        z_cube = calc_cube(z)
        if z_cube == 0:
            break
        idx = bisect_index(num, z_cube)
        result = calculate_difference(z_cube, num, idx)
        print(result)

def main():
    cubes = generate_cubes_list(1, 1111)
    num = generate_num_list(cubes)
    sort_list(num)
    main_loop(num)

main()