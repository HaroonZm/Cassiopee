input_count = int(input())
input_list = [int(element) for element in input().split()]

input_list.sort()
total_sum = sum(input_list)
for element in input_list:
    if total_sum % 2 == 0 or element % 2 == 0:
        continue
    total_sum -= element

result_value = total_sum // 2
print(result_value)