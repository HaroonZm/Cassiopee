a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if c < a + b + 2:
    ans = b + c
else:
    ans = b + a + b + 1

print(ans)