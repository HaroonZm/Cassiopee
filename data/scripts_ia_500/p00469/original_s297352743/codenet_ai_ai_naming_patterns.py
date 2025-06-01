import itertools

while True:
    total_numbers = int(input())
    permutation_length = int(input())
    if (total_numbers, permutation_length) == (0, 0):
        break
    number_list = []
    for _ in range(total_numbers):
        number_list.append(input())
    concatenated_permutations = []
    for permutation in itertools.permutations(number_list, permutation_length):
        concatenated_permutations.append("".join(permutation))
    unique_concatenated_permutations = set(concatenated_permutations)
    print(len(unique_concatenated_permutations))