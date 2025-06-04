import itertools

input_count = int(input())
input_numbers = list(map(int, input().split()))

combinations_pairs = itertools.combinations(input_numbers, 2)

for first_value, second_value in combinations_pairs:
    difference_modulo = abs(first_value - second_value) % (input_count - 1)
    if difference_modulo == 0:
        print(first_value, second_value)
        break