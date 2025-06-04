a, b = map(int, input().split())
res = a - b
if res < 0:
    print(0)
else:
    print(res)