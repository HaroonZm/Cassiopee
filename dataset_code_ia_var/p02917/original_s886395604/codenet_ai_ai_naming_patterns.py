input_count = int(input())
input_values_list = list(map(int, input().split()))

output_values_list = [input_values_list[0]]
for index in range(input_count - 2):
    output_values_list.append(min(input_values_list[index], input_values_list[index + 1]))
output_values_list.append(input_values_list[-1])

print(sum(output_values_list))