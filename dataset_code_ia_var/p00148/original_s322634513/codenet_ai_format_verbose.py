while True:

    try:

        user_input_number = int(input())

        calculated_code_number = ((user_input_number - 1) % 39) + 1

        formatted_code_number = format(calculated_code_number, "02d")

        print("3C" + formatted_code_number)

    except Exception:

        break