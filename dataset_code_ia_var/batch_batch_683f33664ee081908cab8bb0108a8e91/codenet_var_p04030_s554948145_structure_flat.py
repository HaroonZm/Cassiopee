s = input()
ans = []
i = 0
while i < len(s):
    c = s[i]
    if c == '0':
        ans += ['0']
    elif c == '1':
        ans += ['1']
    elif len(ans) != 0:
        ans = ans[:-1]
    i += 1
print(''.join(ans))