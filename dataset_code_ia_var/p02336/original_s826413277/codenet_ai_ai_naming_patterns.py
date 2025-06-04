input_n, input_k = map(int, input().split())
const_modulo = 10**9 + 7

if input_n < input_k:
    print(0)
else:
    product_numerator = 1
    product_denominator = 1
    for index in range(input_n - input_k):
        product_numerator = (product_numerator * (input_n - 1 - index)) % const_modulo
        product_denominator = (product_denominator * (index + 1)) % const_modulo

    inverse_denominator = pow(product_denominator, const_modulo - 2, const_modulo)
    result_value = (product_numerator * inverse_denominator) % const_modulo
    print(result_value)