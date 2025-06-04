input_count = int(input())
input_numbers = list(map(int, input().split()))
input_numbers_sorted = sorted(input_numbers)
adjusted_differences = [input_numbers_sorted[index] - index - 1 for index in range(input_count)]
adjusted_differences_sum = sum(adjusted_differences)
print(adjusted_differences_sum)