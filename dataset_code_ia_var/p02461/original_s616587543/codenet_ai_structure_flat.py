from bisect import bisect_left, bisect_right, insort_left
dict = {}
keytbl = []
q = int(input())
i = 0
while i < q:
    a = input().split()
    if a[0] == '0':
        ki = a[1]
        if ki not in dict:
            insort_left(keytbl, ki)
        dict[ki] = int(a[2])
    elif a[0] == '1':
        ki = a[1]
        if ki in dict:
            print(dict[ki])
        else:
            print(0)
    elif a[0] == '2':
        ki = a[1]
        if ki in dict:
            dict[ki] = 0
    else:
        L = bisect_left(keytbl, a[1])
        R = bisect_right(keytbl, a[2], L)
        j = L
        while j < R:
            k = keytbl[j]
            if dict[k] > 0:
                print(k, dict[k])
            j += 1
    i += 1