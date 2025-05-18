while True:
    n = int(input())
    if n == 0:
        exit()
    s = [None] * n
    for i in range(n):
        s[i] = input()
    ans = [None] * n
    for i, ap in enumerate(s):
        code = [ap[0]]
        for j in range(len(ap) - 1):
            if ap[j] in 'aiueo':
                code.append(ap[j + 1])
        ans[i] = code
    m = max(len(x) for x in ans)
    for k in range(m):
        f = True
        for i in range(n):
            for j in range(i + 1, n):
                if ''.join(ans[i][:k + 1]) == ''.join(ans[j][:k + 1]):
                    f = False
        if f:
            print(k + 1)
            break
    else:
        print(-1)