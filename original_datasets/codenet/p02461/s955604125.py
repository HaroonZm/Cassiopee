from bisect import bisect_left,bisect_right,insort_left

dict = {}
keytbl =[]
q = int(input())
for i in range(q):
    a = list(input().split())
    ki = a[1]
    if a[0] == "0":
        if ki not in dict:
            insort_left(keytbl,ki)
        dict[ki] = int(a[2])
    elif a[0] == "1":
        print(dict[ki] if ki in dict else 0)
    elif a[0] == "2":
        if ki in dict: dict[ki] = 0
    else:
        L =bisect_left(keytbl,a[1])
        R = bisect_right(keytbl,a[2],L)
        for j in range(L,R):
            if dict[keytbl[j]] > 0:
                print(keytbl[j],dict[keytbl[j]])