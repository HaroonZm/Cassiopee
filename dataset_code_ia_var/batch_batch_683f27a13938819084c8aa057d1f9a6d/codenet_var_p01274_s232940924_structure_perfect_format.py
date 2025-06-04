INF = 10 ** 10
MOD = 10 ** 9 + 7

def solve(N):
    HP = [int(input()) for _ in range(N)]
    M = int(input())
    all_magic = []
    single_magic = []
    zero = False
    for _ in range(M):
        a = input().split()
        if zero:
            continue
        if a[2] == 'Single':
            mp = int(a[1])
            dam = int(a[3])
            if mp == 0 and dam > 0:
                zero = True
                continue
            single_magic.append((mp, dam))
        else:
            mp = int(a[1])
            dam = int(a[3])
            if mp == 0 and dam > 0:
                zero = True
                continue
            all_magic.append((mp, dam))
    if zero:
        print(0)
        return

    MAXHP = max(HP) + 5
    dp_single = [INF] * MAXHP
    dp_single[0] = 0
    for p, damage in single_magic:
        for i in range(min(damage, MAXHP)):
            dp_single[i] = min(dp_single[i], p)
        for i in range(damage, MAXHP):
            dp_single[i] = min(dp_single[i], dp_single[i - damage] + p)
    for i in range(MAXHP - 2, -1, -1):
        dp_single[i] = min(dp_single[i], dp_single[i + 1])

    dp_all = [INF] * MAXHP
    dp_all[0] = 0
    for p, damage in all_magic:
        for i in range(min(damage, MAXHP)):
            dp_all[i] = min(dp_all[i], p)
        for i in range(damage, MAXHP):
            dp_all[i] = min(dp_all[i], dp_all[i - damage] + p)

    ans = INF
    for all_dam in range(MAXHP):
        ret = dp_all[all_dam]
        if ret == INF:
            continue
        for h in HP:
            h -= all_dam
            if h > 0:
                ret += dp_single[h]
        ans = min(ans, ret)
    print(ans)

def main():
    while True:
        N = int(input())
        if N == 0:
            return
        solve(N)

if __name__ == '__main__':
    main()