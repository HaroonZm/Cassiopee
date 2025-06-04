M = int(input())
for i in range(M):
    m = int(input())
    y = int(input())
    N = int(input())
    ans = []
    for j in range(N):
        s, p, t = input().split()
        p = float(p)
        t = int(t)
        if s == '0':
            risoku = 0
            _m = m
            for _ in range(y):
                risoku += int(_m * p)
                _m -= t
            result = _m + risoku
            ans.append(result)
        elif s == '1':
            _m = m
            for _ in range(y):
                _m += int(_m * p) - t
            ans.append(_m)
    print(max(ans))