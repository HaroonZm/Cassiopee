a, b = input().split()
a = int(a)
b = int(b)
ans = a + b
if ans > 10:
    ans = 10
if ans == 10:
    print("error")
else:
    print(ans)