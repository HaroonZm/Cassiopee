x = int(input())
ans = 0

if 400 <= x <= 599: ans = 8
if 600 <= x <= 799: ans = 7
if 800 <= x <= 999: ans = 6
if 1000 <= x <= 1199: ans = 5
if 1200 <= x <= 1399: ans = 4
if 1400 <= x <= 1599: ans = 3
if 1600 <= x <= 1799: ans = 2
if 1800 <= x <= 1999: ans = 1

print(ans)