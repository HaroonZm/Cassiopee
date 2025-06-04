import sys

s = input()
ans = ""
i = 0
while i < len(s):
    if s[i] == '0' or s[i] == '1':
        ans += s[i]
    else:
        if len(ans) > 0:
            ans = ans[:-1]
    i += 1
print(ans)