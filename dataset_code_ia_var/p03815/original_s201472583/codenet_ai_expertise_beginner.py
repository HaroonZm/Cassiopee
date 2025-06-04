a = int(input())
s = (a // 11) * 2
reste = a % 11
if reste > 0 and reste <= 6:
    s = s + 1
elif reste >= 7 and reste <= 10:
    s = s + 2
print(s)