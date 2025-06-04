input_length = int(input())
input_values = list(map(int, input().split()))
input_costs = list(map(int, input().split()))
result_sum = 0
for index in range(input_length):
    if input_values[index] > input_costs[index]:
        result_sum += input_values[index] - input_costs[index]
print(result_sum)