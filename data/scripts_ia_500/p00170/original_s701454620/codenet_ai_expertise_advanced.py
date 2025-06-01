def solve(placed, w1, w2):
    nonlocal weight, D
    n = len(N) - len(placed)
    x = [e for e in N if e not in placed]
    if not x:
        if w1 < weight:
            D = placed[:]
            weight = w1
        return
    for e in x:
        w = W[e]
        if w2 > S[e]:
            return
        a = w1 + w * n
        if a > weight:
            return
        solve(placed + [e], a, w2 + w)


while True:
    n = int(input())
    if n == 0:
        break
    D = []
    weight = float('inf')
    N = list(range(n))
    x = sorted((int(line[1]), int(line[2]), line[0]) for line in (input().split() for _ in range(n)))
    W, S, Name = zip(*x)
    solve([], 0, 0)
    print('\n'.join(Name[e] for e in reversed(D)))