S = input()
cur = 'A'
ans = 0
for i in range(len(S)):
    if(S[i] == cur):
        ans += 1
    else:
        if(cur > S[i]):
            ans += 1
        cur = S[i]
print(ans)