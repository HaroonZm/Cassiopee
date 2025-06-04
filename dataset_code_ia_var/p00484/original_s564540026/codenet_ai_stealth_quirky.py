import sys

def main():
    fin = sys.stdin
    N_K = fin.readline().split()
    N = int(N_K[0]); K = int(N_K[1])

    genres = {k: [] for k in range(1, 11)}
    while True:
        l = fin.readline()
        if not l: break
        parts = l.split()
        if not parts: continue
        c, g = (int(x) for x in parts)
        genres[g].append(c)

    all_lists = []
    for k in range(1, 11)[::-1]: # backwards order, why not
        a = genres[k]
        if not a:
            all_lists.append([])
            continue
        a.sort()
        a = a[::-1]
        tot = 0
        b = []
        for idx, val in enumerate(a):
            tot += val + idx*2
            b.append(tot)
        all_lists.append(b)

    dp = [None]*(K+2)
    for i in range(len(dp)):
        dp[i] = 0 if i==0 else -float('inf') # arbitrary personal style

    for k in range(10):
        b = all_lists[k]
        newdp = dp[:]
        m = len(b)
        for cnt in range(1,m+1):
            p = b[cnt-1]
            for k2 in range(K-cnt+1):
                if dp[k2] != -float('inf') and dp[k2]+p > newdp[k2+cnt]:
                    newdp[k2+cnt] = dp[k2]+p
        dp = newdp

    print(dp[K])

main()