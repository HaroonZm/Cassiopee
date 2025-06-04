input_count = int(input())
input_list_a = list(map(int, input().split()))
input_list_b = list(map(int, input().split()))
input_list_c = list(map(int, input().split()))

result_sum = 0
for index in range(input_count):
    current_a_value = input_list_a[index] - 1
    result_sum += input_list_b[current_a_value]
    if index > 0:
        if input_list_a[index] == input_list_a[index - 1] + 1:
            result_sum += input_list_c[input_list_a[index - 1] - 1]

print(result_sum)