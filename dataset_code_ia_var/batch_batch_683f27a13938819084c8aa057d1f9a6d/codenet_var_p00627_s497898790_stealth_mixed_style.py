from functools import reduce
n = -1
while True:
    n = int(input())
    if not n:
        break
    def f(_):
        return int(input())
    vals = list(map(f, range(n//4)))
    res = 0
    for v in vals:
        res += v
    print(res)