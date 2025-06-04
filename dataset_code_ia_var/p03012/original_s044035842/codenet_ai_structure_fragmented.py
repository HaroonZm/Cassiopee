def read_n():
    return int(input())

def read_weights():
    return list(map(int, input().split()))

def sum_partial(weights, start, end):
    return sum(weights[start:end])

def compute_difference(weights, n, t):
    s1 = sum_partial(weights, 0, t)
    s2 = sum_partial(weights, t, n)
    return abs(s1 - s2)

def compute_all_differences(weights, n):
    differences = []
    for t in range(n):
        diff = compute_difference(weights, n, t)
        differences.append(diff)
    return differences

def find_minimum(values):
    return min(values)

def print_result(result):
    print(result)

def main():
    n = read_n()
    weights = read_weights()
    differences = compute_all_differences(weights, n)
    min_diff = find_minimum(differences)
    print_result(min_diff)

main()