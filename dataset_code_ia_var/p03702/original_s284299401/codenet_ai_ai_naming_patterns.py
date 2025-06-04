import itertools
import math

num_total, power_attack, power_secondary = map(int, input().split(" "))
health_list = [int(input()) for _ in range(num_total)]

max_attempts = 10 ** 10
min_attempts = 0

while max_attempts - min_attempts > 1:
    current_attempts = (max_attempts + min_attempts) // 2
    total_special_uses = 0
    for health_value in health_list:
        required_special_uses = math.ceil((health_value - current_attempts * power_secondary) / (power_attack - power_secondary))
        total_special_uses += max(required_special_uses, 0)
    if current_attempts >= total_special_uses:
        max_attempts = current_attempts
    else:
        min_attempts = current_attempts
print(max_attempts)