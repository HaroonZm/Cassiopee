input_string = input()
first_a_index = input_string.find('A')
last_z_index = input_string.rfind('Z')
substring_length = last_z_index - first_a_index + 1
print(substring_length)