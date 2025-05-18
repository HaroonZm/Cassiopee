def dfs(s):
    for t in G[s]:
        if not used[t]:
            used[t] = 1
            dfs(t)
    res.append(s)
def rdfs(s, l):
    for t in RG[s]:
        if label[t] is None:
            label[t] = l
            rdfs(t, l)

while 1:
    n = int(input())
    if n == 0:
        break
    G = [[] for i in range(n)]
    RG = [[] for i in range(n)]
    P = []
    for i in range(n):
        p, m, *A = input().split()
        P.append(float(p))
        for t in map(int, A):
            G[i].append(t-1)
            RG[t-1].append(i)
    used = [0]*n
    res = []
    for i in range(n):
        if not used[i]:
            used[i] = 1
            dfs(i)
    label = [None]*n; k = 0
    for i in reversed(res):
        if label[i] is None:
            label[i] = k
            rdfs(i, k)
            k += 1
    GP = [1.]*k; GF = [0]*k
    for s in range(n):
        l = label[s]
        GP[l] *= P[s]
        for t in G[s]:
            if label[s] != label[t]:
                GF[label[t]] += 1
    ans = 1.
    for i in range(k):
        if GF[i] == 0:
            ans *= 1.-GP[i]
    print("%.9f" % (ans))