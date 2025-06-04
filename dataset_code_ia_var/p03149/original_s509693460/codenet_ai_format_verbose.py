user_input_numbers = input().split()

integer_numbers_list = [int(number_string) for number_string in user_input_numbers]

sorted_integer_numbers_list = sorted(integer_numbers_list)

if sorted_integer_numbers_list[0] != 1:
    print("NO")
elif sorted_integer_numbers_list[1] != 4:
    print("NO")
elif sorted_integer_numbers_list[2] != 7:
    print("NO")
elif sorted_integer_numbers_list[3] != 9:
    print("NO")
else:
    print("YES")