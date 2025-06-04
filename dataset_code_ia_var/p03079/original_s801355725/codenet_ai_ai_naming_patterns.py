input_values_list = list(map(int, input().split()))
value_first = input_values_list[0]
value_second = input_values_list[1]
value_third = input_values_list[2]

if value_first == value_second and value_first == value_third:
    print("Yes")
else:
    print("No")