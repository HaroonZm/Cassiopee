user_input_length = int(input())
user_input_string = input()
half_of_input_length = int(user_input_length // 2)

for current_iteration in range(half_of_input_length):

    last_character = user_input_string[user_input_length - 1]
    symmetric_character = user_input_string[user_input_length - 1 - half_of_input_length]

    if last_character == symmetric_character:
        user_input_length -= 1

if user_input_length == half_of_input_length:
    print("Yes")
else:
    print("No")