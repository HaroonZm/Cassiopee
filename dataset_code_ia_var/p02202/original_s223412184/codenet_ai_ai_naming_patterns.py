input_count = int(input())
input_values = list(map(int, input().split()))
duplicate_sum = sum(input_values) - (input_count * (input_count + 1)) // 2
print(duplicate_sum)