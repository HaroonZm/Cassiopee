input_string = input()
step_width = int(input())
current_index = 0
result_string = ""
while current_index < len(input_string):
    result_string += input_string[current_index]
    current_index += step_width
print(result_string)