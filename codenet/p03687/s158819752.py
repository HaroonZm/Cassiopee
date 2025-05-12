import sys
S = list(sys.stdin.readline().rstrip())
chars = [chr(ord("a") + i) for i in range(26)]
ans = 10**5
for c in chars:
    if c not in S:
        continue
    cnt = 0
    S_copy = S.copy()
    while len(set(S_copy)) > 1:
        S_tmp = []
        for i in range(len(S_copy) - 1):
            if S_copy[i] == c or S_copy[i + 1] == c:
                S_tmp.append(c)
            else:
                S_tmp.append(S[i])
        S_copy = S_tmp.copy()
        cnt += 1
    ans = min(ans, cnt)
print(ans)