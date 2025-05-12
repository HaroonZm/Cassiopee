s = list(str(input()))
t = list(str(input()))

ans = 'No'
for i in range(len(s)):
    tmp = s[i:] + s[:i]
    if tmp == t:
        ans = 'Yes'
        break
print(ans)