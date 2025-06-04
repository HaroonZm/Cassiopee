import array

def calc_check_digit(seq_idx):
    if 1 <= seq_idx <= 6:
        return seq_idx + 1
    else:
        return seq_idx - 5

def is_sequence_valid(num_seq):
    weighted_sum = 0
    for idx in range(1, 12):
        weighted_sum += num_seq[idx] * calc_check_digit(idx)
    modulo_result = weighted_sum % 11
    expected_digit = 0 if modulo_result <= 1 else (11 - modulo_result)
    return num_seq[0] == expected_digit

def convert_string_to_array(num_str):
    return array.array("B", map(int, num_str[::-1]))

def find_unique_candidate(input_str):
    valid_digit_candidates = set()
    for replacement_digit in range(10):
        candidate_str = input_str.replace("?", str(replacement_digit))
        candidate_seq = convert_string_to_array(candidate_str)
        if is_sequence_valid(candidate_seq):
            valid_digit_candidates.add(replacement_digit)
    if len(valid_digit_candidates) == 1:
        return valid_digit_candidates.pop()
    else:
        return -1

def run_main():
    user_input = input()
    result = find_unique_candidate(user_input)
    print("MULTIPLE" if result == -1 else result)

if __name__ == '__main__':
    run_main()