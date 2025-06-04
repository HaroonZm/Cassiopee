num_elements = int(input())
input_sequence = list(map(int, input().split()))
output_sequence = [0] * num_elements

output_sequence[0] = input_sequence[0]
output_sequence[num_elements - 1] = input_sequence[num_elements - 2]

for index in range(num_elements - 2):
    output_sequence[index + 1] = min(input_sequence[index], input_sequence[index + 1])

print(sum(output_sequence))