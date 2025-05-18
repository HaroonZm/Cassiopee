import bisect

q = int(input())
S = []

for i in range(q):
    query, *n = input().split()
    x = int(n[0])
    index_left = bisect.bisect_left(S, x)
    index_right = bisect.bisect_right(S, x)

    # insert
    if query[0] == "0":
        x = int(n[0])
        S.insert(index_left, x)
        print(len(S))

    # find
    elif query[0] == "1":
        x = int(n[0])
        print(index_right - index_left)

    # delete
    elif query[0] == "2":
        x = int(n[0])
        S[index_left:index_right] = []

    # dump
    else:
        L = int(n[0])
        R = int(n[1])
        
        index_left = bisect.bisect_left(S, L)
        index_right = bisect.bisect_right(S, R)

        [print(i) for i in S[index_left:index_right]]