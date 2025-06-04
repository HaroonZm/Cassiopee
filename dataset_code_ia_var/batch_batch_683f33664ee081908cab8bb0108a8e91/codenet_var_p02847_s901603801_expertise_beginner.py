S = input()
D = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
count = 0
for day in D:
    days_left = 7 - count
    if day == S:
        print(days_left)
    count = count + 1