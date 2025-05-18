S, T = list(str(input()).lower()), list(str(input()).lower())
res = 0
for i in range(0, len(S)):
    if S[i] != T[i]:
        res += 1
print(res)