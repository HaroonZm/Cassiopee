num_elements = int(input())
values_list = list(map(int, input().split()))

sum_result = values_list[0] + values_list[-1]

for index in range(num_elements - 2):
    sum_result += min(values_list[index], values_list[index + 1])
print(sum_result)