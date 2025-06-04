input_count = int(input())
input_values = list(map(int, input().split()))

even_index_elements = []
odd_index_elements = []

for index in range(input_count):
    if index % 2 == 0:
        even_index_elements.append(input_values[index])
    else:
        odd_index_elements.append(input_values[index])

if input_count % 2 == 0:
    output_sequence = odd_index_elements[::-1] + even_index_elements
else:
    output_sequence = even_index_elements[::-1] + odd_index_elements

print(*output_sequence)