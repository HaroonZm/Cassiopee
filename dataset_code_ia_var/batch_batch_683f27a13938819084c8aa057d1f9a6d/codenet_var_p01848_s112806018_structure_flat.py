while 1:
    n = int(input())
    if n == 0:
        break
    G = [[] for i in range(n)]
    RG = [[] for i in range(n)]
    P = []
    for i in range(n):
        parts = input().split()
        p = parts[0]
        m = int(parts[1])
        A = parts[2:]
        P.append(float(p))
        for t in map(int, A):
            G[i].append(t-1)
            RG[t-1].append(i)
    used = [0]*n
    res = []
    stack = []
    for i in range(n):
        if not used[i]:
            stack.append(i)
            while stack:
                cur = stack[-1]
                if not used[cur]:
                    used[cur] = 1
                    child_found = False
                    for t in G[cur]:
                        if not used[t]:
                            stack.append(t)
                            child_found = True
                            break
                    if not child_found:
                        res.append(cur)
                        stack.pop()
                else:
                    if cur not in res:
                        res.append(cur)
                    stack.pop()
    label = [None]*n
    k = 0
    stack = []
    for idx in range(len(res)-1, -1, -1):
        i = res[idx]
        if label[i] is None:
            label[i] = k
            stack.append(i)
            while stack:
                cur = stack.pop()
                for t in RG[cur]:
                    if label[t] is None:
                        label[t] = k
                        stack.append(t)
            k += 1
    GP = [1.]*k
    GF = [0]*k
    for s in range(n):
        l = label[s]
        GP[l] *= P[s]
        for t in G[s]:
            if label[s] != label[t]:
                GF[label[t]] += 1
    ans = 1.
    for i in range(k):
        if GF[i] == 0:
            ans *= 1. - GP[i]
    print("%.9f" % (ans))