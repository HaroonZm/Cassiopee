input_number = int(input())
input_list = list(map(int, input().split()))
expected_sum = input_number * (input_number + 1) // 2
actual_sum = sum(input_list)
difference_result = actual_sum - expected_sum
print(difference_result)