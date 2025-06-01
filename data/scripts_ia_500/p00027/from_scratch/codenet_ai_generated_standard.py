days = ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"]
month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    m, d = map(int, input().split())
    if m == 0 and d == 0:
        break
    total_days = sum(month_days[:m-1]) + d - 1
    print(days[total_days % 7])