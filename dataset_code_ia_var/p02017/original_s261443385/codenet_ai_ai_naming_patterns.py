height_value, width_value, pos_x_value, pos_y_value = map(int, input().split())
if (height_value * width_value) % 2 == 1 and (pos_x_value + pos_y_value) % 2 == 1:
    print("No")
else:
    print("Yes")