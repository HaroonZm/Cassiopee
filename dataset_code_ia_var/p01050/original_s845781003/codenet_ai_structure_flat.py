from collections import defaultdict

S = input()
S = sorted(S)
S = list(map(ord, S))
ans = 0
while len(S) > 0:
    mn = S[0]
    S.remove(mn)
    nxt = mn + 1
    succ = 1
    while True:
        found = False
        for i in range(len(S)):
            if S[i] == nxt:
                del S[i]
                succ += 1
                nxt += 1
                found = True
                break
        if not found:
            break
    if succ >= 3:
        ans += 3
    else:
        ans += succ
print(ans)