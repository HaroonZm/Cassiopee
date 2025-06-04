modulus = 998244353

factorial_table_size = 1 << 20

factorial = [0] * factorial_table_size
inverse_factorial = [0] * factorial_table_size
modular_inverse = [0] * factorial_table_size

factorial[0] = 1
inverse_factorial[0] = 1
factorial[1] = 1
inverse_factorial[1] = 1
modular_inverse[1] = 1

for index in range(2, factorial_table_size):
    factorial[index] = factorial[index - 1] * index % modulus
    modular_inverse[index] = (
        modulus - modular_inverse[modulus % index] * (modulus // index) % modulus
    )
    inverse_factorial[index] = (
        inverse_factorial[index - 1] * modular_inverse[index] % modulus
    )

input_value_A, input_value_B = map(int, input().split())
if input_value_A < input_value_B:
    input_value_A, input_value_B = input_value_B, input_value_A

intermediate_sum = 0
power_of_two_mod = 1

for current_index in range(1, input_value_B + 1):
    intermediate_sum += (
        power_of_two_mod
        * factorial[input_value_A + input_value_B - current_index]
        * inverse_factorial[input_value_B - current_index]
        * inverse_factorial[input_value_A]
    )
    power_of_two_mod = power_of_two_mod * 2 % modulus

final_result = (
    intermediate_sum
    * factorial[input_value_A]
    * factorial[input_value_B]
    * inverse_factorial[input_value_A + input_value_B]
    + input_value_A
) % modulus

print(final_result)