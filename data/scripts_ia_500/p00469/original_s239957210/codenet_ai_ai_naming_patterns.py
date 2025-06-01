import itertools

while True:
    input_count_total = int(input())
    input_count_permutations = int(input())
    if input_count_total == 0 and input_count_permutations == 0:
        break
    input_elements = []
    for element_index in range(input_count_total):
        input_elements.append(input())
    
    permutations_list = list(itertools.permutations(input_elements, input_count_permutations))
    concatenated_permutations = []
    for permutation in permutations_list:
        concatenated_permutations.append(''.join(permutation))
    unique_permutations = list(set(concatenated_permutations))
    print(len(unique_permutations))