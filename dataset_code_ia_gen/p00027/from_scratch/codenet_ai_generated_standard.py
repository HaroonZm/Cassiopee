days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    m, d = map(int, input().split())
    if m == 0 and d == 0:
        break
    total_days = sum(days_in_month[:m-1]) + d - 1
    print(days[(3 + total_days) % 7])