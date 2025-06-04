while True:

    try:
        user_input = input()
        integer_value = int(user_input)
    except Exception:
        break

    remainder_after_division_by_39 = integer_value - (integer_value // 39) * 39

    formatted_number = remainder_after_division_by_39 if remainder_after_division_by_39 % 39 != 0 else 39

    formatted_output = "3C{:02d}".format(formatted_number)

    print(formatted_output)