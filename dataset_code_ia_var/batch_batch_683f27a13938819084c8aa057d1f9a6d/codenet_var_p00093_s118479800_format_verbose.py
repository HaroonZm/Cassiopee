has_printed_before = False

while True:
    user_input = raw_input().split()
    start_year, end_year = map(int, user_input)

    if (start_year, end_year) == (0, 0):
        break

    if has_printed_before:
        print
    else:
        has_printed_before = True

    leap_years_in_range = [
        year for year in xrange(start_year, end_year + 1)
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    ]

    if not leap_years_in_range:
        print "NA"
    else:
        print "\n".join(map(str, leap_years_in_range))