import sys

input_string = input()

first_a_position = input_string.find("A")
last_z_position = input_string.rfind("Z")

substring_length = last_z_position - first_a_position + 1

print("{}".format(substring_length))