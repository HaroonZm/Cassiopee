input_value = int(input())
highest_power_of_two = 1 << (input_value.bit_length() - 1)
difference_value = input_value - highest_power_of_two

if difference_value == 0:
    print("No")
else:
    print("Yes")
    print(1, 2)
    print(2, 3)
    print(3, input_value + 1)
    print(input_value + 1, input_value + 2)
    print(input_value + 2, input_value + 3)
    for loop_index in range(4, input_value, 2):
        print(loop_index, loop_index + 1)
        print(loop_index + input_value, loop_index + input_value + 1)
        print(1 + input_value, loop_index + input_value)
        print(1 + input_value, loop_index + 1)
    if (~input_value) & 1:
        print(input_value, highest_power_of_two + input_value)
        xor_value = input_value ^ highest_power_of_two ^ 1
        print(input_value + input_value, xor_value)