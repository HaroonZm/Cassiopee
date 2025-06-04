input_count = int(input())

for input_index in range(input_count):
    total_days = 0
    start_year, start_month, start_day = map(int, input().split())

    total_days += 1  # Include the current day

    if start_year % 3 == 0 or start_month % 2 == 1:
        total_days += 20 - start_day
    else:
        total_days += 19 - start_day

    for month_index in range(start_month + 1, 11):
        if start_year % 3 == 0 or month_index % 2 == 1:
            total_days += 20
        else:
            total_days += 19

    for year_offset in range(1, 1000 - start_year):
        current_year = start_year + year_offset
        for month_number in range(1, 11):
            if current_year % 3 == 0 or month_number % 2 == 1:
                total_days += 20
            else:
                total_days += 19

    print(total_days)