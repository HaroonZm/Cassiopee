height, width = [int(value) for value in input().split(" ")]

city_map = []
for row_index in range(height):
    current_line = input()
    row_timers = []
    last_cloud_timer = -1000
    for column_char in current_line:
        if column_char == "c":
            last_cloud_timer = 0
            row_timers.append(last_cloud_timer)
        else:
            last_cloud_timer += 1
            row_timers.append(last_cloud_timer)
    city_map.append(row_timers)

for row_index in range(height):
    for column_index in range(width):
        if city_map[row_index][column_index] < 0:
            city_map[row_index][column_index] = "-1"
        else:
            city_map[row_index][column_index] = str(city_map[row_index][column_index])

for row in city_map:
    print(" ".join(row))