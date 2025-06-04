#!/usr/bin/env python3

input_num1, input_num2, input_num3 = map(int, input().split())
const_modulo = int(1e9+7)

if input_num3 < input_num1:
    result_value = input_num3 % const_modulo
else:
    factor_k = (input_num3 - input_num2) // (input_num1 - input_num2)
    result_value = (input_num3 + input_num2 * factor_k)
    result_value %= const_modulo
print(result_value)