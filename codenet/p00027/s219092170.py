from datetime import date
import calendar

while True:
    m, d = map(int, input().split())
    if not m:
        break
    print(calendar.day_name[date(2004, m, d).weekday()])