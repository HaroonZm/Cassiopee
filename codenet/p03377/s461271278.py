a, b, x = map(int, input().split())
if a > x:
    print("NO")
else:
    if a+b < x:
        print("NO")
    else:
        print("YES")