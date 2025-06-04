n = int(input())
S = input()

ans = 0
for i in range(1, n+1):
    X = S[:i]
    Y = S[i:]
    tmp = []
    for x in X:
        if x in Y:
            if x not in tmp:
                tmp.append(x)
    if len(tmp) > ans:
        ans = len(tmp)
print(ans)