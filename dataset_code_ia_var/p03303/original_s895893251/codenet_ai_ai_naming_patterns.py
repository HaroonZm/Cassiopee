user_input_string = input()
user_input_step = int(input())
output_string = user_input_string[::user_input_step]
print(output_string)