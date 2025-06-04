stack_positions = []
pool_areas = []
total_area = 0
current_index = 0

for char in input():
    if char == "\\":
        stack_positions.append(current_index)
    elif char == "/" and stack_positions:
        left_index = stack_positions.pop()
        pool_width = current_index - left_index
        total_area += pool_width
        while pool_areas and pool_areas[-1][0] > left_index:
            pool_width += pool_areas[-1][1]
            pool_areas.pop()
        pool_areas.append((left_index, pool_width))
    current_index += 1

print(total_area)
if pool_areas:
    print(len(pool_areas), *[area for (_, area) in pool_areas])
else:
    print(0)