import bisect

q = int(input())
S = []

for _ in range(q):
    query, *params = input().split()
    if query == "0":
        x = int(params[0])
        idx = bisect.bisect_left(S, x)
        S.insert(idx, x)
        print(len(S))
    elif query == "1":
        x = int(params[0])
        left = bisect.bisect_left(S, x)
        right = bisect.bisect_right(S, x)
        print(right - left)
    elif query == "2":
        x = int(params[0])
        left = bisect.bisect_left(S, x)
        right = bisect.bisect_right(S, x)
        S[left:right] = []
    else:
        L = int(params[0])
        R = int(params[1])
        left = bisect.bisect_left(S, L)
        right = bisect.bisect_right(S, R)
        for i in S[left:right]:
            print(i)