input_string = input()

def has_symmetric_prefix(prefix_length, string_value):
    is_symmetric = True
    for index in range(prefix_length):
        if string_value[index] != string_value[prefix_length + index]:
            is_symmetric = False
    return is_symmetric

for candidate_length in range(len(input_string) - 1, 1, -1):
    if candidate_length % 2 == 1:
        continue
    half_length = candidate_length // 2
    if has_symmetric_prefix(half_length, input_string[:candidate_length]):
        print(candidate_length)
        break