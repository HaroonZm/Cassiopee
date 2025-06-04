def compute_gcd(value_a, value_b):
    if value_a < value_b:
        value_a, value_b = value_b, value_a
    if value_a % value_b == 0:
        return value_b
    else:
        return compute_gcd(value_b, value_a % value_b)

input_count = int(input())
input_values = list(map(int, input().split()))

current_lcm = input_values[0]
for index in range(1, input_count):
    current_lcm = current_lcm * input_values[index] / compute_gcd(current_lcm, input_values[index])
print(int(current_lcm))