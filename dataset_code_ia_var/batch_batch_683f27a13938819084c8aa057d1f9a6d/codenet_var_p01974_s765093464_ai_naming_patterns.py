import itertools

input_count = int(input())
input_numbers = list(map(int, input().split()))

for pair_combination in itertools.combinations(input_numbers, 2):
    pair_difference = abs(pair_combination[0] - pair_combination[1])
    if pair_difference % (input_count - 1) == 0:
        print(pair_combination[0], pair_combination[1])
        break