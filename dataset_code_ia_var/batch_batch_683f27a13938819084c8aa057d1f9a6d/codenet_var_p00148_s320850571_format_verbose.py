while True:

    try:
        user_input_string = raw_input()

        user_input_integer = int(user_input_string)

    except EOFError:
        break

    remainder_when_divided_by_39 = user_input_integer % 39

    if remainder_when_divided_by_39 == 0:
        print '3C39'
    else:
        formatted_remainder = str(remainder_when_divided_by_39).zfill(2)
        print '3C' + formatted_remainder