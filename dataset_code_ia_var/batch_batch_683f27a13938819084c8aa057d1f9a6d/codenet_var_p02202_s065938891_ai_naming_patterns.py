input_count = int(input())
input_values = list(map(int, input().split()))
expected_sum = input_count * (input_count + 1) // 2
actual_sum = sum(input_values)
difference = actual_sum - expected_sum
print(difference)