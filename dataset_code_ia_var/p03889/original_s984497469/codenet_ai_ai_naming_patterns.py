mirror_char_map = { 'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p' }
input_string = raw_input()
reversed_input_string = input_string[::-1]
mirrored_string = ''.join(mirror_char_map[char] for char in reversed_input_string)
is_mirror_symmetric = (input_string == mirrored_string)
mirror_check_result = ['No', 'Yes'][is_mirror_symmetric]
print mirror_check_result