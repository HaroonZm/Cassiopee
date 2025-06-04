user_input = input()
first_a_index = user_input.find('A')
last_z_index = user_input.rfind('Z')
substring_length = last_z_index - first_a_index + 1
print(substring_length)