input_string = input()
input_length = len(input_string)

count_x = input_string.count('x')

if count_x <= 7:
    print('YES')
else:
    print('NO')