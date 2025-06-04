input_count = int(input())
input_values = list(map(int, input().split()))
even_indexed_values = []
odd_indexed_values = []
for index in range(input_count):
    if index % 2 == 0:
        even_indexed_values.append(input_values[index])
    else:
        odd_indexed_values.append(input_values[index])

if input_count % 2 == 0:
    for value in reversed(odd_indexed_values):
        print(value, end=' ')
    for value in even_indexed_values:
        print(value, end=' ')
else:
    for value in reversed(even_indexed_values):
        print(value, end=' ')
    for value in odd_indexed_values:
        print(value, end=' ')