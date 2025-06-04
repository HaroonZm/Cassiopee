input_string, az_flag, az_count = input(), 1, 0
for char in input_string:
    if char == 'A':
        az_flag = 0
    elif char == 'Z' and not az_flag:
        az_flag, az_count = 1, az_count + 1
print('AZ' * az_count if az_count else -1)