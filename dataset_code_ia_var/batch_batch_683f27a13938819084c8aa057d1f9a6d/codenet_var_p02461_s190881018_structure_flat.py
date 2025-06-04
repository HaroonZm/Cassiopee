from bisect import bisect_left, bisect_right, insort_left

a = []
q = int(input())
i = 0
while i < q:
    a.append(input().split())
    i += 1
S = {}
W = []
i = 0
while i < q:
    if a[i][0] == '0':
        if not a[i][1] in S:
            insort_left(W, a[i][1])
        S[a[i][1]] = int(a[i][2])
    elif a[i][0] == '1':
        if a[i][1] in S:
            print(S[a[i][1]])
        else:
            print(0)
    elif a[i][0] == '2':
        if a[i][1] in S:
            S[a[i][1]] = 0
    else:
        L = bisect_left(W, a[i][1])
        R = bisect_right(W, a[i][2])
        j = L
        while j < R:
            if S[W[j]] > 0:
                print(W[j], S[W[j]])
            j += 1
    i += 1