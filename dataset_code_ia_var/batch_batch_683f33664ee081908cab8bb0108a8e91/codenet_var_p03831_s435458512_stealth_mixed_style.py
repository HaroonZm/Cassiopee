def ex():
    from sys import stdin
    f = lambda: list(map(int, stdin.readline().split()))
    args = f()
    n, a, b = args[0], args[1], args[2]
    lst = list(map(int, stdin.readline().split()))
    result = 0
    for i in range(n-1):
        diff = lst[i+1] - lst[i]
        tmp = diff * a
        if tmp < b:
            result = result + tmp
        else:
            result += b
    print(result)

import sys
if sys.argv[0]:
    ex()