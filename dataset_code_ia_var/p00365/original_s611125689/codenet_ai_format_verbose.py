first_date_components = tuple(map(int, input().split()))
second_date_components = tuple(map(int, input().split()))

list_of_dates = sorted([first_date_components, second_date_components])

first_date_year, first_date_month, first_date_day = list_of_dates[0]
second_date_year, second_date_month, second_date_day = list_of_dates[1]

year_difference = second_date_year - first_date_year

has_passed_anniversary = (
    second_date_month > first_date_month or
    (second_date_month == first_date_month and second_date_day > first_date_day)
)

result = year_difference + (1 if has_passed_anniversary else 0)

print(result)