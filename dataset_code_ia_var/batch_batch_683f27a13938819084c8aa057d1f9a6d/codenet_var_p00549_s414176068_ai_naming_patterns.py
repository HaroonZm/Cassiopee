input_length = int(input())
input_string = input()
prefix_count_j = 0
prefix_count_o = 0
prefix_count_i = 0
prefix_j_occurrences = [0] * input_length
for idx_prefix, char_prefix in enumerate(input_string):
    if char_prefix == 'J':
        prefix_count_j += 1
    elif char_prefix == 'O':
        prefix_count_o += prefix_count_j
    else:
        prefix_count_i += prefix_count_o
    prefix_j_occurrences[idx_prefix] = prefix_count_j

suffix_count_i = 0
suffix_count_o = 0
suffix_count_j = 0
suffix_i_occurrences = [0] * input_length
for idx_suffix, char_suffix in enumerate(reversed(input_string)):
    if char_suffix == 'I':
        suffix_count_i += 1
    elif char_suffix == 'O':
        suffix_count_o += suffix_count_i
    else:
        suffix_count_j += suffix_count_o
    suffix_i_occurrences[input_length - 1 - idx_suffix] = suffix_count_i

max_result = max(prefix_count_o, suffix_count_o)
for idx_max in range(input_length):
    max_result = max(max_result, prefix_j_occurrences[idx_max] * suffix_i_occurrences[idx_max])
print(max_result + prefix_count_i)