input_numbers_list = [int(element) for element in input().split()]

height_value = input_numbers_list[0]
rate_value = input_numbers_list[1]

sum_value = height_value + rate_value

if sum_value >= 1:
    print("1")
elif sum_value <= -1:
    print("-1")
elif sum_value == 0:
    print("0")