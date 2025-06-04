number_of_inputs_processed = 0

while True:

    try:
        start_year, end_year = map(int, raw_input().split())

        if start_year + end_year == 0:
            break

        if number_of_inputs_processed > 0:
            print ""

        found_leap_year = False

        for year in range(start_year, end_year + 1):
            is_divisible_by_4 = (year % 4 == 0)
            is_not_divisible_by_100_or_divisible_by_400 = (year % 100 != 0 or year % 400 == 0)

            if is_divisible_by_4 and is_not_divisible_by_100_or_divisible_by_400:
                print year
                found_leap_year = True

        if not found_leap_year:
            print "NA"

        number_of_inputs_processed += 1

    except:
        break