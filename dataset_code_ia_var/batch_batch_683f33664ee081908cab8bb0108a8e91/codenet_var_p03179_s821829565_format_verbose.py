import sys

standard_input_reader = sys.stdin.readline

def count_valid_permutations(sequence_length, inequality_signs_string):
    MODULO = int(1e9 + 7)
    
    dynamic_programming = [1] * sequence_length

    for current_index in range(1, sequence_length):
        cumulative_sums = list(dynamic_programming)
        
        for cumulative_index in range(1, sequence_length - current_index + 1):
            cumulative_sums[cumulative_index] += cumulative_sums[cumulative_index - 1]
            cumulative_sums[cumulative_index] %= MODULO
        
        total_cumulative_sum = cumulative_sums[sequence_length - current_index]
        previous_index = current_index - 1
        
        for permutation_start_position in range(sequence_length - current_index):

            if inequality_signs_string[previous_index] == ">":
                dynamic_programming[permutation_start_position] = cumulative_sums[permutation_start_position]

            else:
                dynamic_programming[permutation_start_position] = (total_cumulative_sum - cumulative_sums[permutation_start_position] + MODULO) % MODULO
    
    return dynamic_programming[0]

sequence_length = int(standard_input_reader())  # 2 <= sequence_length <= 30000

inequality_signs_string = standard_input_reader().rstrip()  # len(inequality_signs_string) = sequence_length - 1

print(count_valid_permutations(sequence_length, inequality_signs_string))