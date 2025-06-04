import math

input_integer_total, input_integer_threshold = map(int, input().split())

probability_accumulator = 0.0

for current_integer in range(1, input_integer_total + 1):
    power_exponent = max(0, math.ceil(math.log(input_integer_threshold / current_integer, 2)))
    probability_increment = (1.0 / input_integer_total) * (0.5) ** power_exponent
    probability_accumulator += probability_increment

print(probability_accumulator)