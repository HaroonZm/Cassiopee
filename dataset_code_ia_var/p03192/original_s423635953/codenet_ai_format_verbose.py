from sys import stdin

input_number_string = stdin.readline().rstrip()

input_number_string = str(input_number_string)

count_of_digit_2 = 0

if len(input_number_string) == 4:
    
    if input_number_string[0] == "2":
        count_of_digit_2 += 1
    
    if input_number_string[1] == "2":
        count_of_digit_2 += 1
    
    if input_number_string[2] == "2":
        count_of_digit_2 += 1
    
    if input_number_string[3] == "2":
        count_of_digit_2 += 1

print(count_of_digit_2)