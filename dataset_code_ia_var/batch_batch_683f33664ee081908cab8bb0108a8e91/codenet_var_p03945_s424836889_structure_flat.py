S = input()
ans = 0
i = 0
while i < len(S) - 1:
    if S[i] != S[i+1]:
        ans += 1
    i += 1
print(ans)