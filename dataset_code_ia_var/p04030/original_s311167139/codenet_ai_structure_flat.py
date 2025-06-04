N = input()
ans = ''
i = 0
while i < len(N):
    if ans == '' and N[i] == 'B':
        i += 1
        continue
    if ans == '' and N[i] != 'B':
        ans = N[i]
    elif N[i] == 'B':
        ans = ans[:-1]
    else:
        ans = ans + N[i]
    i += 1
print(ans)