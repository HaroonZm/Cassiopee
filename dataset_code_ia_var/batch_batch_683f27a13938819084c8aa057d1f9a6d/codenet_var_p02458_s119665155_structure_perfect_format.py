from bisect import bisect_left, bisect_right, insort_left

d = {}
keytbl = []
cnt = 0
q = int(input())
for _ in range(q):
    a = input().split()
    ki = int(a[1])
    if a[0] == '0':
        if ki not in d:
            d[ki] = 1
            insort_left(keytbl, ki)
        else:
            d[ki] += 1
        cnt += 1
        print(cnt)
    elif a[0] == '1':
        print(d[ki] if ki in d else 0)
    elif a[0] == '2':
        if ki in d:
            cnt -= d[ki]
            d[ki] = 0
    else:
        L = bisect_left(keytbl, int(a[1]))
        R = bisect_right(keytbl, int(a[2]), L)
        for j in range(L, R):
            for _ in range(d[keytbl[j]]):
                print(keytbl[j])