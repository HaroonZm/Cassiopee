while True:
    input_height, input_width = [int(value) for value in input().split()]
    if input_height == 0 and input_width == 0:
        break
    for row_index in range(input_height):
        print("#" * input_width)
    print("")