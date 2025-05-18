q = int(input())
S = set([])

for i in range(q):
    query, x = list(map(int, input().split()))

    # insert
    if query == 0:
        S.add(x)
        print(len(S))

    # find
    elif query == 1:
        if x in S:
            print(1)
        else:
            print(0)

    # delete
    else:
        if x in S:
            S.remove(x)