allowed_chars = 'qwertyuiopasdfghjklzxcvbnm'
input_str = input()
result_flag = 'yes'

for current_char in input_str:
    if current_char in allowed_chars:
        allowed_chars = allowed_chars.replace(current_char, '')
    else:
        result_flag = 'no'
        break

print(result_flag)