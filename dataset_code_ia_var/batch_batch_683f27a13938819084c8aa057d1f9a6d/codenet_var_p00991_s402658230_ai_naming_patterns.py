from math import factorial as math_factorial

def calculate_combinations(total_steps, steps_in_direction):
    return math_factorial(total_steps) // (math_factorial(steps_in_direction) * math_factorial(total_steps - steps_in_direction))

width, height, a_x, a_y, b_x, b_y = map(int, input().split())
delta_x = min(width - abs(a_x - b_x), abs(a_x - b_x))
delta_y = min(height - abs(a_y - b_y), abs(a_y - b_y))
result_count = 1

if delta_x * 2 == width:
    result_count *= 2
if delta_y * 2 == height:
    result_count *= 2

result_count *= calculate_combinations(delta_x + delta_y, delta_x)
print(result_count % 100000007)