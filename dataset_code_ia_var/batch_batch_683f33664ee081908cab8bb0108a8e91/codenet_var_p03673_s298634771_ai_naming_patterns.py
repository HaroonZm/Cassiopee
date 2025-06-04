input_count = int(input())
input_values = [int(value) for value in input().split()]

elements_even_index = []
elements_odd_index = []

for index in range(input_count):
    if index % 2 == 0:
        elements_odd_index.append(input_values[index])
    else:
        elements_even_index.append(input_values[index])

if input_count % 2 == 0:
    elements_even_index.reverse()
    output_sequence = elements_even_index + elements_odd_index
    print(*output_sequence)
else:
    elements_odd_index.reverse()
    output_sequence = elements_odd_index + elements_even_index
    print(*output_sequence)