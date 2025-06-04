first_point, second_point, third_point, max_distance = map(int, input().split())

is_directly_reachable = abs(first_point - third_point) <= max_distance

is_reachable_via_second_point = (abs(first_point - second_point) <= max_distance 
                                 and abs(second_point - third_point) <= max_distance)

if is_directly_reachable:
    print("Yes")

elif is_reachable_via_second_point:
    print("Yes")

else:
    print("No")