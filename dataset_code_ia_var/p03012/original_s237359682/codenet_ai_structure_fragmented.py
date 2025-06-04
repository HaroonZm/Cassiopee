import sys

def read_input():
    return sys.stdin.readline().rstrip()

def read_integer():
    return int(read_input())

def read_integer_list():
    return list(map(int, read_input().split()))

def initialize_prefix_sum_array(size):
    return [0 for _ in range(size + 1)]

def build_prefix_sum(weights, prefix_sum_array, n):
    for i in range(n):
        update_prefix_sum(prefix_sum_array, i, weights[i])

def update_prefix_sum(prefix_sum_array, index, value):
    prefix_sum_array[index + 1] = prefix_sum_array[index] + value

def calculate_total_weight(prefix_sum_array, n):
    return prefix_sum_array[n]

def compute_absolute_difference(prefix_sum_array, total_weight, split_index):
    left_sum = prefix_sum_array[split_index + 1]
    right_sum = total_weight - left_sum
    return abs(left_sum - right_sum)

def find_minimum_difference(prefix_sum_array, n):
    total_weight = calculate_total_weight(prefix_sum_array, n)
    minimum_difference = 10 ** 9 + 7
    for i in range(n):
        difference = compute_absolute_difference(prefix_sum_array, total_weight, i)
        minimum_difference = update_minimum(minimum_difference, difference)
    return minimum_difference

def update_minimum(current_minimum, new_value):
    return min(current_minimum, new_value)

def print_result(result):
    print(result)

def solve():
    n = read_integer()
    weights = read_integer_list()
    prefix_sum_array = initialize_prefix_sum_array(n)
    build_prefix_sum(weights, prefix_sum_array, n)
    minimum_difference = find_minimum_difference(prefix_sum_array, n)
    print_result(minimum_difference)

if __name__ == '__main__':
    solve()