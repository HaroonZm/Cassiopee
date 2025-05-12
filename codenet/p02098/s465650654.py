a = int(input())
b = int(input())
a = a % 360
b = b % 360
if a > b :
    a, b = b, a
if b - a > 180 :
    a += 360
t = abs((a - b) / 2)
ans = min(a, b) + t
ans = ans % 360
print('{:6f}'.format(ans))