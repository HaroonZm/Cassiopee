import math

input_number = int(input())

factorial_result = math.factorial(input_number)
modulo_value = 10 ** 9 + 7

result = factorial_result % modulo_value

print(result)