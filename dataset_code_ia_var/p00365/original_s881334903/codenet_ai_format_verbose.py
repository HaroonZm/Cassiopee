first_year, first_month, first_day = map(int, input().split())
second_year, second_month, second_day = map(int, input().split())

first_date_is_after_second = (
    first_year > second_year or
    (
        first_year == second_year and
        (
            first_month > second_month or
            (first_month == second_month and first_day > second_day)
        )
    )
)

if first_date_is_after_second:
    first_year, second_year = second_year, first_year
    first_month, second_month = second_month, first_month
    first_day, second_day = second_day, first_day

has_full_year_passed = (
    first_month < second_month or
    (first_month == second_month and first_day < second_day)
)

if has_full_year_passed:
    number_of_full_years = second_year - first_year + 1
else:
    number_of_full_years = second_year - first_year

print(number_of_full_years)