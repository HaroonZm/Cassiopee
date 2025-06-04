start_position, intermediary_position, target_position, maximum_distance = map(int, input().split())

if abs(start_position - target_position) <= maximum_distance:
    print("Yes")

elif abs(start_position - intermediary_position) <= maximum_distance and abs(intermediary_position - target_position) <= maximum_distance:
    print("Yes")

else:
    print("No")