input_string = input()

stride_length = int(input())

current_index = 0

resulting_substring = ""

while current_index < len(input_string):
    resulting_substring += input_string[current_index]
    current_index += stride_length

print(resulting_substring)