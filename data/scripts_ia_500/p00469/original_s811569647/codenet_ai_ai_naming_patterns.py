import itertools
while True:
    input_line = raw_input()
    if input_line == "0 0":
        break
    else:
        permutation_length = input()
    if permutation_length == 0:
        break
    input_list = [raw_input() for _ in range(int(input_line))]
    unique_permutations = set()
    for permutation_tuple in itertools.permutations(input_list, permutation_length):
        concatenated_string = "".join(permutation_tuple)
        unique_permutations.add(concatenated_string)
    print len(unique_permutations)