def read_input():
    n, k = map(int, input().split())
    return n, k

def read_numbers(n):
    numbers = []
    for _ in range(n):
        numbers.append(int(input()))
    return numbers

def calculate_differences(li):
    differences = []
    for i in range(len(li)-1):
        differences.append(calculate_difference(li[i], li[i+1]))
    return differences

def calculate_difference(a, b):
    return b - a - 1

def sort_descending(diff):
    return sorted(diff, reverse=True)

def sum_differences(diff, start_index):
    total = 0
    for i in range(start_index, len(diff)):
        total += diff[i]
    return total

def main():
    n, k = read_input()
    li = read_numbers(n)
    diff = calculate_differences(li)
    diff_sorted = sort_descending(diff)
    result = calculate_result(n, diff_sorted, k)
    print(result)

def calculate_result(n, diff_sorted, k):
    return n + sum_differences(diff_sorted, k - 1)

main()