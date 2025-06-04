input_count = int(input())
input_numbers = [int(number_str) for number_str in input().split()]
import math
current_lcm = input_numbers[0]
for current_number in input_numbers[1:]:
    current_lcm = (current_number * current_lcm) // math.gcd(current_lcm, current_number)
print(current_lcm)