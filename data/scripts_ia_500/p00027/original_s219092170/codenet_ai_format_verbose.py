from datetime import date
import calendar


while True:
    input_month_day = input()
    month_str, day_str = input_month_day.split()
    
    month = int(month_str)
    day = int(day_str)
    
    if month == 0:
        break
    
    fixed_year = 2004
    
    corresponding_date = date(fixed_year, month, day)
    
    weekday_index = corresponding_date.weekday()
    
    weekday_name = calendar.day_name[weekday_index]
    
    print(weekday_name)