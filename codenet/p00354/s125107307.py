from datetime import date
 
weekdays = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
 
x = int(input())
idx = date(2017, 9, x).weekday()
print(weekdays[idx])