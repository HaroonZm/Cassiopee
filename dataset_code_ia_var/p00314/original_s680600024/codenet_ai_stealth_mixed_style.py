def resolv():
    N = int(input())
    from functools import reduce
    ps = input().split()
    arr = [int(x) for x in ps]
    arr.sort(key=lambda x: -x)
    r = 0
    i = 0
    while i < N:
        if arr[i] >= i + 1:
            r = i + 1
        i += 1
    print(r)
resolv()