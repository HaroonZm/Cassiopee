import sys
readline = sys.stdin.readline
write = sys.stdout.write

gcd = lambda m, n: gcd(n, m % n) if n else m
lcm = lambda m, n: m // gcd(m, n) * n

while True:
    N_line = readline()
    if not N_line:
        break
    N = int(N_line)
    if N == 0:
        break

    pp = [13, 17, 19, 23]
    E = [[0]*i for i in range(25)]
    Q = []
    for _ in range(N):
        raw = readline()
        if not raw.strip():
            raw = readline()
        d, t, *qs = map(int, raw.strip().split())
        if len(qs) < d:
            rem = d - len(qs)
            while rem > 0:
                extra = list(map(int, readline().strip().split()))
                qs.extend(extra)
                rem -= len(extra)
        qs = qs[t:] + qs[:t]
        Ed = E[d]
        for i in range(d):
            Ed[i] += qs[i]
    L = 13860
    V = [0]*L
    for i in range(1, 25):
        if i in pp:
            continue
        if i <= 12:
            Ei = E[i]
            Ej = E[2*i]
            for j in range(2*i):
                Ej[j] += Ei[j % i]
        else:
            Ei = E[i]
            if i == 16:
                for j in range(8):
                    Ei[j] = max(Ei[j+8], Ei[j])
                Ej = E[24]
                for j in range(24):
                    Ej[j] += Ei[j % 8]
            elif i == 24:
                for j in range(12):
                    Ei[j] = max(Ei[j+12], Ei[j])
                for j in range(L):
                    V[j] += Ei[j % 12]
            else:
                for j in range(L):
                    V[j] += Ei[j % i]
    ans = max(V)
    for i in pp:
        ans += max(E[i])
    write("%d\n" % ans)