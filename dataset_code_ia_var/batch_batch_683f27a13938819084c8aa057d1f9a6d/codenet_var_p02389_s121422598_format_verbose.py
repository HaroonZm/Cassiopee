user_input_list = input().split()

rectangle_length = int(user_input_list[0])
rectangle_width = int(user_input_list[1])

rectangle_area = rectangle_length * rectangle_width

rectangle_perimeter = 2 * rectangle_length + 2 * rectangle_width

print(rectangle_area, rectangle_perimeter)