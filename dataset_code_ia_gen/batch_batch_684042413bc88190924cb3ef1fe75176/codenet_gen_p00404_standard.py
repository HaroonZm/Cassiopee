x,y = map(int,input().split())
n = max(abs(x), abs(y))
s = (2*n-1)**2 if n>0 else 0
D = 8*n if n>0 else 1
if n == 0:
    k = 0
elif x > n:
    k = s + (n - y)
elif y > n:
    k = s + (3*n + x)
elif x < -n:
    k = s + (5*n + y)
else:
    k = s + (7*n - x)
print((k % 3) + 1)