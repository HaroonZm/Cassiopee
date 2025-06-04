import itertools

def find_max_sum_by_greedy(sequence):
    while len(sequence) >= 3:
        if sequence[-3] + sequence[-2] > sequence[-1]:
            return sequence.pop() + sequence.pop() + sequence.pop()
        else:
            sequence.pop()

def find_max_sum_by_bruteforce(sequence):
    while len(sequence) >= 3 and sequence[-3] + sequence[-2] <= sequence[-1]:
        sequence.pop()
    maximal_sum = 0
    for combination in itertools.combinations(sequence[-10:], 6):
        for first_group_indices in itertools.combinations(range(6), 3):
            group_one = []
            group_two = []
            for index in range(6):
                if index in first_group_indices:
                    group_one.append(combination[index])
                else:
                    group_two.append(combination[index])
            if group_one[0] + group_one[1] > group_one[2] and group_two[0] + group_two[1] > group_two[2]:
                maximal_sum = max(maximal_sum, sum(combination))
    return maximal_sum

def compute_solution(input_sequence):
    global_max_sum = 0

    working_sequence_greedy = list(input_sequence)
    greedy_sum_first = find_max_sum_by_greedy(working_sequence_greedy)
    greedy_sum_second = find_max_sum_by_greedy(working_sequence_greedy)
    if greedy_sum_first is not None and greedy_sum_second is not None:
        global_max_sum = max(global_max_sum, greedy_sum_first + greedy_sum_second)

    working_sequence_bruteforce = list(input_sequence)
    bruteforce_sum = find_max_sum_by_bruteforce(working_sequence_bruteforce)
    global_max_sum = max(global_max_sum, bruteforce_sum)

    return global_max_sum

input_count = int(input())
input_values = sorted([int(input()) for _ in range(input_count)])
final_result = compute_solution(input_values)
print(final_result)