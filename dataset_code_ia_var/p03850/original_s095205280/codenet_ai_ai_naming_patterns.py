input_value = input()
input_tokens = raw_input().split()

value_a = int(input_tokens[0])
value_b = value_c = -10 ** 18

for operator_token, number_token in zip(input_tokens[1::2], map(int, input_tokens[2::2])):
    if operator_token == "+":
        temp_d = max(value_b - number_token, value_c + number_token)
        value_a_new = max(value_a + number_token, temp_d)
        value_b_new = temp_d
        value_c_new = value_c + number_token
    else:
        temp_d = max(value_b + number_token, value_c - number_token)
        value_a_new = max(value_a - number_token, temp_d)
        value_b_new = value_a_new
        value_c_new = temp_d
    value_a, value_b, value_c = value_a_new, value_b_new, value_c_new

print(max(value_a, value_b, value_c))