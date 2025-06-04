S = input().strip()
ans = ''
i = 0
while i < len(S):
    c = S[i]
    if c == 'B':
        if len(ans) > 0:
            ans = ans[:-1]
    else:
        ans += c
    i += 1
print(ans)