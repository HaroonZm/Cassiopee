import math

total_elements, division_factor = map(int, input().split())

step_count = 1
accumulated_value = 1

while True:
    
    required_value = math.ceil(accumulated_value / division_factor)
    
    if required_value + accumulated_value > total_elements:
        break
    
    accumulated_value += required_value
    step_count += 1

print(step_count)