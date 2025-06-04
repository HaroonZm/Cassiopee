input_length = int(input())
input_string = input()

uppercase_first_half = [chr(ascii_code) for ascii_code in range(ord('A'), ord('A') + 13)]
uppercase_second_half = [chr(ascii_code) for ascii_code in range(ord('A') + 13, ord('A') + 26)]
lowercase_first_half = [chr(ascii_code) for ascii_code in range(ord('a'), ord('a') + 13)]
lowercase_second_half = [chr(ascii_code) for ascii_code in range(ord('a') + 13, ord('a') + 26)]

counter_array = [0, 0]
for character in input_string:
    if character in uppercase_first_half:
        counter_array[0] += 1
    elif character in uppercase_second_half:
        counter_array[0] -= 1
    elif character in lowercase_first_half:
        counter_array[1] += 1
    elif character in lowercase_second_half:
        counter_array[1] -= 1

result_string = ''
if counter_array[0] < 0:
    result_string += 'N' * abs(counter_array[0])
else:
    result_string += 'A' * counter_array[0]
if counter_array[1] < 0:
    result_string += 'n' * abs(counter_array[1])
else:
    result_string += 'a' * counter_array[1]

print(len(result_string))
print(result_string)