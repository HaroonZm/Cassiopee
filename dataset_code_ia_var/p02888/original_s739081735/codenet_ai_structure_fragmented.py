from bisect import bisect_left

def read_input():
    n = get_int()
    l = get_int_list()
    return n, l

def get_int():
    return int(input())

def get_int_list():
    return list(map(int, input().split()))

def sort_list(l):
    return sorted(l)

def calculate_pairs(n, l):
    ans = 0
    for i in generate_range(n-1):
        for j in generate_range2(i+1, n):
            count = count_valid_k(l, i, j)
            ans = add(ans, count)
    return ans

def generate_range(limit):
    return range(limit)

def generate_range2(start, end):
    return range(start, end)

def count_valid_k(l, i, j):
    target = sum_elements(l[i], l[j])
    valid_k = find_bisect_left(l, target)
    diff = subtract(valid_k, j+1)
    return diff

def sum_elements(a, b):
    return a + b

def find_bisect_left(l, value):
    return bisect_left(l, value)

def subtract(a, b):
    return a - b

def add(a, b):
    return a + b

def print_result(ans):
    print(ans)

def main():
    n, l = read_input()
    l = sort_list(l)
    ans = calculate_pairs(n, l)
    print_result(ans)

main()