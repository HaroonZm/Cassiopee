number_of_integers_to_read = int(input())

input_integers_list = []

while len(input_integers_list) < number_of_integers_to_read:
    user_input = input()
    input_integers_list.extend(list(map(int, user_input.split())))

appeared_numbers_set = set()

for starting_index in range(number_of_integers_to_read):
    max_subsequence_length = min(3, number_of_integers_to_read - starting_index)
    for subsequence_length in range(0, max_subsequence_length):
        subsequence_as_string = "".join(map(str, input_integers_list[starting_index : starting_index + subsequence_length + 1]))
        appeared_numbers_set.add(int(subsequence_as_string))

for candidate_number in range(1000):
    if candidate_number not in appeared_numbers_set:
        print(candidate_number)
        break