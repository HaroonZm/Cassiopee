user_input = input().split()
user_input_ints = [int(element) for element in user_input]
rectangle_area = user_input_ints[0] * user_input_ints[1]
rectangle_perimeter = (user_input_ints[0] + user_input_ints[1]) * 2
print(rectangle_area, rectangle_perimeter)