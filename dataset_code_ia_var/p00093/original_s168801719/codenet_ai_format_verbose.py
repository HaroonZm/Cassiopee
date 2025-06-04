import sys

is_first_case = False

for input_line in sys.stdin:

    start_year, end_year = map(int, input_line.split())

    if start_year == 0 and end_year == 0:
        break

    leap_years_list = []

    for year in range(start_year, end_year + 1):
        if year % 4 == 0:
            if year % 400 == 0:
                leap_years_list.append(year)
            elif year % 100 != 0:
                leap_years_list.append(year)

    if is_first_case:
        print

    if leap_years_list == []:
        print "NA"
    else:
        for leap_year in leap_years_list:
            print leap_year

    is_first_case = True