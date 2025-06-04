input_str_list = list(input())

input_str_set = set(input_str_list)

if len(input_str_list) == len(input_str_set):
    print('yes')
else:
    print('no')