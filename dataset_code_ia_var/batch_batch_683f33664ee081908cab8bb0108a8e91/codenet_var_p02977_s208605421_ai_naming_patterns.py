input_value = int(input())
if input_value <= 2 or input_value == 4:
    print("No")
elif input_value == 3:
    print("Yes")
    for iteration_index in range(5):
        print(iteration_index + 1, iteration_index + 2)
elif input_value % 2 == 0:
    bit_length_value = input_value.bit_length()
    power_of_two_comparison = 2 ** (bit_length_value - 1)
    if input_value == power_of_two_comparison:
        print("No")
    else:
        print("Yes")
        print(1, 2)
        print(2, 3)
        print(3, input_value + 1)
        print(input_value + 1, input_value + 2)
        print(input_value + 2, input_value + 3)
        for loop_index in range(4, input_value):
            print(input_value + 1, loop_index)
            if loop_index % 2 == 0:
                print(loop_index, loop_index + input_value + 1)
            else:
                print(loop_index, loop_index + input_value - 1)
        node_first = 2 ** (bit_length_value - 1)
        node_second = (input_value + 1) - 2 ** (bit_length_value - 1)
        print(node_first, input_value)
        print(node_second, 2 * input_value)
else:
    print("Yes")
    print(1, 2)
    print(2, 3)
    print(3, input_value + 1)
    print(input_value + 1, input_value + 2)
    print(input_value + 2, input_value + 3)
    for loop_index in range(4, input_value + 1):
        print(1, loop_index)
        if loop_index % 2 == 0:
            print(loop_index, loop_index + input_value + 1)
        else:
            print(loop_index, loop_index + input_value - 1)