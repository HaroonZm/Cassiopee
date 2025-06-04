input_n, input_a, input_b, input_c, input_d = map(int, input().split())
result_values = []
if input_n % input_a != 0:
    result_values.append((input_n // input_a + 1) * input_b)
else:
    result_values.append(int((input_n / input_a) * input_b))
if input_n % input_c != 0:
    result_values.append((input_n // input_c + 1) * input_d)
else:
    result_values.append(int((input_n / input_c) * input_d))
print(min(result_values))