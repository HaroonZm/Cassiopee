input_source = input()
input_target = input()

is_prefix_match = input_target.startswith(input_source)
is_length_valid = len(input_target) == len(input_source) + 1

if is_prefix_match and is_length_valid:
    print('Yes')
else:
    print('No')