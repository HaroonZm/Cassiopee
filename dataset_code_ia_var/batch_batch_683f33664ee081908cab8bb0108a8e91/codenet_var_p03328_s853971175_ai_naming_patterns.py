width, end_value = map(int, input().split())
range_difference = end_value - width
accumulated_height = 0
for height_increment in range(1, range_difference + 1):
    accumulated_height += height_increment
print(accumulated_height - end_value)