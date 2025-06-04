user_input_string = input()

input_contains_a = "a" in user_input_string
input_contains_b = "b" in user_input_string
input_contains_c = "c" in user_input_string

if input_contains_a and input_contains_b and input_contains_c:
    print("Yes")
else:
    print("No")