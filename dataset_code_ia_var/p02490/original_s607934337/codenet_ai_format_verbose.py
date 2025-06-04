while True:

    first_integer_input, second_integer_input = map(int, raw_input().split())

    if first_integer_input == 0 and second_integer_input == 0:
        break

    if first_integer_input < second_integer_input:
        print "%d %d" % (first_integer_input, second_integer_input)
    else:
        print "%d %d" % (second_integer_input, first_integer_input)