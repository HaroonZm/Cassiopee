x = int(input())
a = x // 11
b = x % 11
if b == 0:
    res = a * 2
elif b <= 6:
    res = a * 2 + 1
else:
    res = a * 2 + 2
print(res)