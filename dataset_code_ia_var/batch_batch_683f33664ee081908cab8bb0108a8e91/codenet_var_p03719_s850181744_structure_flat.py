a,b,c = map(int, input().split())
if a <= c:
    if c <= b:
        print("Yes")
    else:
        print("No")
else:
    print("No")