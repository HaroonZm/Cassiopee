import sys

input_height, input_width = map(int, input().split())

min_difference = 10**10

partition_areas_list = []

if input_height % 3 == 0 or input_width % 3 == 0:
    print(0)
    sys.exit()

for partition_height_primary in [input_height // 3, (input_height // 3) + 1]:
    remaining_height = input_height - partition_height_primary
    area_primary = partition_height_primary * input_width
    if (remaining_height * input_width) % 2 == 0:
        area_secondary = area_tertiary = (remaining_height * input_width) // 2
        partition_areas_list.append([area_primary, area_secondary, area_tertiary])
    else:
        area_secondary = (remaining_height // 2) * input_width
        area_tertiary = ((remaining_height // 2) + 1) * input_width
        partition_areas_list.append([area_primary, area_secondary, area_tertiary])
        width_even_part = (input_width // 2) * remaining_height
        width_odd_part = ((input_width // 2) + 1) * remaining_height
        partition_areas_list.append([area_primary, width_even_part, width_odd_part])

for partition_width_primary in [input_width // 3, (input_width // 3) + 1]:
    remaining_width = input_width - partition_width_primary
    area_primary = partition_width_primary * input_height
    if (remaining_width * input_height) % 2 == 0:
        area_secondary = area_tertiary = (remaining_width * input_height) // 2
        partition_areas_list.append([area_primary, area_secondary, area_tertiary])
    else:
        area_secondary = (remaining_width // 2) * input_height
        area_tertiary = ((remaining_width // 2) + 1) * input_height
        partition_areas_list.append([area_primary, area_secondary, area_tertiary])
        height_even_part = (input_height // 2) * remaining_width
        height_odd_part = ((input_height // 2) + 1) * remaining_width
        partition_areas_list.append([area_primary, height_even_part, height_odd_part])

for partition_areas in partition_areas_list:
    max_area = max(partition_areas)
    min_area = min(partition_areas)
    min_difference = min(min_difference, max_area - min_area)

print(min_difference)