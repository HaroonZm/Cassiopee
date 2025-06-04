def read_input():
    return input().split()

def to_int_list(str_list):
    return list(map(int, str_list))

def parse_initial_values(split_line):
    return tuple(map(int, split_line))

def read_A():
    return to_int_list(input().split())

def calculate_range(start, end):
    return range(start, end)

def in_list(element, lst):
    return element in lst

def increment_if_in_list(i, A):
    return 1 if in_list(i, A) else 0

def calculate_cost(start, end, A):
    cost = 0
    for i in calculate_range(start, end):
        cost += increment_if_in_list(i, A)
    return cost

def find_min_cost(cost_b, cost_a):
    return min(cost_b, cost_a)

def main():
    line = read_input()
    N, M, X = parse_initial_values(line)
    A = read_A()
    cost_a = calculate_cost(X, N, A)
    cost_b = calculate_cost(0, X, A)
    result = find_min_cost(cost_b, cost_a)
    print(result)

main()