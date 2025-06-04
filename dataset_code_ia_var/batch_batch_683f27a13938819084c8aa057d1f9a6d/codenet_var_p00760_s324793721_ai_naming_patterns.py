num_cases = int(input())
result_list = []
for case_index in range(num_cases):
    total_days = 0
    year_input, month_input, day_input = map(int, input().split())
    if year_input % 3 == 0:
        total_days += (10 - month_input) * 20 + (20 - day_input + 1)
        year_input += 1
    else:
        full_months = (10 - month_input)
        leap_months = full_months // 2
        normal_months = full_months - leap_months
        total_days += normal_months * 20 + leap_months * 19 + (19 - day_input + 1) + 5
        year_input += 1
    remaining_years = 1000 - year_input
    leap_years = remaining_years // 3
    normal_years = remaining_years - leap_years
    total_days += leap_years * 200 + normal_years * 195
    result_list.append(total_days)
for result_value in result_list:
    print(result_value)