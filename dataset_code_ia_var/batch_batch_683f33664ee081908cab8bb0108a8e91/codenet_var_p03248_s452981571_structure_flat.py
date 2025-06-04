s = input()
n = len(s)
if s[0] == "0" or s[-1] == "1":
    print(-1)
    exit()
i = 0
invalid = False
while i < n - 1:
    if s[i] != s[n - i - 2]:
        print(-1)
        exit()
    i += 1
ans = []
now = 0
i = 0
while i < n - 1:
    if s[i] == "1":
        ans.append(str(now + 1) + " " + str(i + 2))
        now = i + 1
    else:
        ans.append(str(now + 1) + " " + str(i + 2))
    i += 1
i = 0
while i < len(ans):
    print(ans[i])
    i += 1