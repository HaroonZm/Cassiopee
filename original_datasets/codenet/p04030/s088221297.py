import sys

stdin = sys.stdin
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline()

s = input()
ans = ""
for i in range(len(s)):
    if s[i] == '0' or s[i] == '1':
        ans += s[i]
    else:
        if len(ans) > 0:
            ans = ans[:-1]
print(ans)