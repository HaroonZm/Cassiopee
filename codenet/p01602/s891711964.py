n = int(input())
b = 0
ans = True
for _ in range(n):
    p, x = input().split()
    x = int(x)

    if p == "(":
        b += x
    else:
        b -= x
        if b < 0:
            ans = False

if ans:
    if b == 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")