def read_integer():
    return int(input())

def read_integer_list():
    return list(map(int, input().split()))

def pop_first_element(lst):
    value = lst.pop(0)
    return value, lst

def list_to_set(lst):
    return set(lst)

def create_universal_set(n):
    return set(range(1, n + 1))

def complement_set(base_set, universal_set):
    return universal_set - base_set

def intersection(set1, set2):
    return set1 & set2

def union(set1, set2):
    return set1 | set2

def compute_result(n, a, b, c):
    universal = create_universal_set(n)
    a_bar = complement_set(a, universal)
    part1 = intersection(a_bar, c)
    part2 = intersection(b, c)
    ans = union(part1, part2)
    return ans

def print_length_of_set(s):
    print(len(s))

def main():
    n = read_integer()
    a_list = read_integer_list()
    X, a_list = pop_first_element(a_list)
    a_set = list_to_set(a_list)

    b_list = read_integer_list()
    Y, b_list = pop_first_element(b_list)
    b_set = list_to_set(b_list)

    c_list = read_integer_list()
    Z, c_list = pop_first_element(c_list)
    c_set = list_to_set(c_list)

    ans = compute_result(n, a_set, b_set, c_set)
    print_length_of_set(ans)

main()