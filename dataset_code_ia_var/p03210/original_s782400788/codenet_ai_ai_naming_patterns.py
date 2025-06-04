user_input_value = int(input())
is_valid_prime_length = (user_input_value == 3) or (user_input_value == 5) or (user_input_value == 7)
if is_valid_prime_length:
    print("YES")
else:
    print("NO")