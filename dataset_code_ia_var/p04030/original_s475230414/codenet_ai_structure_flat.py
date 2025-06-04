s = input()
l = len(s)
ans = []
i = 0
while i < l:
    if s[i] == '0':
        ans.append('0')
    elif s[i] == '1':
        ans.append('1')
    else:
        if ans != []:
            ans.pop(-1)
    i += 1
n = len(ans)
j = 0
while j < n:
    if j < n - 1:
        print(ans[j], end="")
    else:
        print(ans[j])
    j += 1