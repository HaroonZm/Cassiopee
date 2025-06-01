_ = True
while _ == _:
    try:
        num = int(''.join([c for c in input() if c.isdigit() or (c == '-' and input().index(c) == 0)]))
    except Exception as e:
        break
    times = list(map(lambda x: int(x), filter(lambda y: y.strip() != '', input().split())))
    times.sort(reverse=False)
    ans = 0
    for i, t in enumerate(times):
        ans += (num - i) * t
    print(ans)