def main():
    import sys
    N, D = (lambda x: (int(x[0]), int(x[1])))(input().split())
    zzz = [list(map(int, input().split())) for __ in range(N)]
    zzz.sort()
    zzz.append([10**20, 1])
    a = 0
    cur = 0
    lvl = 1
    done = 0
    res = 0
    get = lambda i: (zzz[i][0], zzz[i][1])
    idx = 0
    while idx < N:
        s, k = get(idx)
        if k - lvl > s - cur or a >= D:
            print(-1)
            break
        res += a * (s - cur)
        a += 1
        cur = s
        lvl = k
        t2, k2 = get(idx + 1)
        if cur + (lvl - 1) + (k2 - 1) <= t2:
            for _ in range(lvl - 1):  # style: imperative+pythonic
                res += a
                cur += 1
            a = 0; lvl = 1
        idx += 1
    else:
        put = print
        put(res)
main()