mirror_map = { 'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p' }
input_string = raw_input()
reversed_string = input_string[::-1]
mirrored_string = ''.join(mirror_map[char] for char in reversed_string)
is_mirrored = (input_string == mirrored_string)
result_list = ['No', 'Yes']
print result_list[is_mirrored]