first_input_year, first_input_month, first_input_day = map(int, input().split())
second_input_year, second_input_month, second_input_day = map(int, input().split())

if first_input_month == second_input_month and first_input_day == second_input_day:
    print(abs(first_input_year - second_input_year))
    exit()

if first_input_year > second_input_year:
    first_date_numeric = 100 * first_input_month + first_input_day
    second_date_numeric = 100 * second_input_month + second_input_day
elif first_input_year < second_input_year:
    first_date_numeric = 100 * second_input_month + second_input_day
    second_date_numeric = 100 * first_input_month + first_input_day
else:
    print(1)
    exit()

if first_date_numeric > second_date_numeric:
    print(abs(first_input_year - second_input_year) + 1)
else:
    print(abs(first_input_year - second_input_year))