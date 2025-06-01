n = int(input())

for _ in range(n):
    x, y, b, p = map(int, input().split())
    if b < 5 and p < 2:
        ans = min((x*b+y*p), ((x*5+y*2)*0.8))
    elif b >= 5 and p < 2:
        ans = min((x*b+y*p), ((x*b+y*2)*0.8))
    elif b < 5 and p >= 2:
        ans = min((x*b+y*p), ((x*5+y*p)*0.8))
    else:
        ans = (x*b+y*p)*0.8

    print(int(ans))