def solve():
    from sys import stdin
    f_i = stdin
    N, C = map(int, f_i.readline().split())
    ranking = [(0, i) for i in range(1, N + 1)]
    ranking.insert(0, (-1000000000 * C, 0))
    score = [0] * (N + 1)
    from bisect import bisect_left, insort
    ans = []
    for i in range(C):
        cmd = f_i.readline().split()
        if cmd[0] == '0':
            t, p = map(int, cmd[1:])
            pre_score = score[t]
            pre_rec = (pre_score, t)
            ranking.pop(bisect_left(ranking, pre_rec))
            new_score = pre_score - p
            score[t] = new_score
            insort(ranking, (new_score, t))
        else:
            m = int(cmd[1])
            p, t = ranking[m]
            ans.append(' '.join(map(str, (t, -p))))
    print('\n'.join(ans))

solve()