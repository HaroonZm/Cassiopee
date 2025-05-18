#!/usr/bin/env python3
while True:
    n = int(input())
    if n == 0:
        break
    s = ['a' + input() for _ in range(n)]
    m = max(len(x) for x in s)
    for i in range(1, m + 1):
        dic = dict()
        for x in s:
            code = ''
            for j in range(len(x)):
                if len(code) == i:
                    break
                if j > 0 and x[j - 1] in ['a', 'i', 'u', 'e', 'o']:
                    code += x[j]
            if code in dic:
                break
            dic[code] = True
        else:
            print(i)
            break
    else:
        print(-1)