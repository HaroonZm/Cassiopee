import math

while 1:
    N = int(input())
    if N == 0:
        break
    lst = list(map(int, input().split()))
    v = sum(lst)
    x = (math.sqrt(8*v + 1) - 1) / 2
    if x != int(x):
        print(-1)
        continue

    result = -1
    for count in range(10000):
        ok = True
        for i in range(len(lst)):
            if lst[i] != i + 1:
                ok = False
                break
        if ok:
            result = count
            break
        spam = len(lst)
        tmp = []
        for x in lst:
            if x-1 > 0:
                tmp.append(x-1)
        tmp.append(spam)
        lst = tmp
    print(result)