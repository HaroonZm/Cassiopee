q = int(input())
S = set([])

for i in range(q):
    query, x = list(map(int, input().split()))

    # insert
    if query == 0:
        S.add(x)
        print(len(S))

    # find
    else:
        if x in S:
            print(1)
        else:
            print(0)