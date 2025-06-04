input_multiplier, modulus_limit, target_value = map(int, input().split())
generated_values_list = []
for current_index in range(modulus_limit):
    generated_value = (current_index * input_multiplier) % modulus_limit
    generated_values_list.append(generated_value)
if target_value in generated_values_list:
    print('YES')
else:
    print('NO')