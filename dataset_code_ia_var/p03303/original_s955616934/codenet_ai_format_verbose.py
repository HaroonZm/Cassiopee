original_string = input()

step_width = int(input())

result_string = ""

for character_index in range(len(original_string)):

    if character_index % step_width == 0:

        result_string += original_string[character_index]

print(result_string)