import math
import sys

sys_input = sys.stdin.readline

input_value_k = int(sys_input())

sequence_length_n = 512
calc_pattern = 0
combinatorial_values = []
for idx_seq in range(sequence_length_n):
    comb_val = math.factorial(7 + idx_seq) // math.factorial(idx_seq) // math.factorial(7)
    combinatorial_values.append(comb_val)
combinatorial_values.reverse()

max_letter_count = 600 * 7
result_strings = ["FESTIVA" for _ in range(sequence_length_n)]
for idx_comb, comb_item in enumerate(combinatorial_values):
    result_strings[idx_comb] += ("L" * (input_value_k // comb_item))
    input_value_k %= comb_item
result_strings.reverse()
print("".join(str(output_str) for output_str in result_strings))