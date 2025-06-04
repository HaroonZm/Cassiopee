s = '0'
s += input()
N = len(s) - 1
ok = True
if s[N] == '1' or s[1] == '0':
    print(-1)
    ok = False
if ok:
    l = 1
    r = N - 1
    while l <= r:
        if s[l] != s[r]:
            print(-1)
            ok = False
            break
        l += 1
        r -= 1
if ok:
    root = 1
    i = 2
    while i <= N:
        print(str(root) + ' ' + str(i))
        if s[i - 1] == '1':
            root = i
        i += 1