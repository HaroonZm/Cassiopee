from collections import deque
ca = ord('a')
while 1:
    N = int(input())
    if N == 0:
        break
    G = [[] for i in range(26)]
    S = [0]*26; T = [0]*26
    for i in range(N):
        word = input()
        s = ord(word[0]) - ca; t = ord(word[-1]) - ca
        S[s] += 1; T[t] += 1
        G[s].append(t)
    ok = 1
    for i in range(26):
        if S[i] != T[i]:
            ok = 0
    if ok:
        que = deque()
        U = [0]*26
        for i in range(26):
            if S[i]:
                que.append(i)
                U[i] = 1
                break
        while que:
            v = que.popleft()
            for w in G[v]:
                if U[w]:
                    continue
                U[w] = 1
                que.append(w)
        for i in range(26):
            if S[i] and not U[i]:
                ok = 0
    print("OK" if ok else "NG")