a = int(input())
s = (a // 11) * 2
r = a % 11
if r > 0 and r <= 6:
    s = s + 1
if r >= 7 and r <= 10:
    s = s + 2
print(s)