while True:
    try:
        input_string = str(input())

        joi_substring_count = 0
        ioi_substring_count = 0

        for current_index in range(len(input_string) - 2):

            current_three_characters = input_string[current_index : current_index + 3]

            if current_three_characters == "JOI":
                joi_substring_count += 1

            elif current_three_characters == "IOI":
                ioi_substring_count += 1

        print(joi_substring_count)
        print(ioi_substring_count)

    except Exception:
        break