import sys
input = sys.stdin.readline

while True:
    T, D, L = map(int, input().split())
    if T == 0 and D == 0 and L == 0:
        break
    x = [int(input()) for _ in range(T)]
    intervals = []
    last_wet = -D - 1  # temps où le point a séché
    for i in range(T):
        if x[i] >= L:
            if i + 1 > last_wet + D:
                # nouveau intervalle humide
                start = i + 1
                end = i + 1 + D
                intervals.append([start, end])
            else:
                # raccorde intervalle précédent
                intervals[-1][1] = i + 1 + D
            last_wet = i + 1
    # fusionner intervalles qui se chevauchent
    merged = []
    for s,e in intervals:
        if not merged or merged[-1][1] < s:
            merged.append([s,e])
        else:
            merged[-1][1] = max(merged[-1][1], e)
    # compter tps humide dans [1, T]
    ans = 0
    for s,e in merged:
        ans += max(0, min(e, T+1) - s)
    print(ans)