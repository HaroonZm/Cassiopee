import math

input_count = int(input())
input_numbers = list(map(int, input().split()))

lcm_result = input_numbers[0]
for index in range(input_count):
    lcm_result = lcm_result * input_numbers[index] // math.gcd(lcm_result, input_numbers[index])
print(lcm_result)