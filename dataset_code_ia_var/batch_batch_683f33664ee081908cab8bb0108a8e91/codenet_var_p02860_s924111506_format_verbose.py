import sys

input_string_length = int(input())

input_character_list = list(str(input()))

if input_string_length % 2 == 1:
    print("No")
else:
    half_length = input_string_length // 2

    for index in range(half_length):
        if input_character_list[index] != input_character_list[index + half_length]:
            print("No")
            sys.exit()
    print("Yes")