import itertools

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

if P == Q:
    print(0)
else:
    PQ = [P, Q]
    PQ = sorted(PQ)
    li = list(range(1, N + 1))
    i = 0
    j = 0
    a = []
    stop = False
    for v in itertools.permutations(li, N):
        j += 1
        if PQ[i] == v:
            a.append(j)
            if i == 1:
                stop = True
                break
            else:
                i += 1
    ans = a[1] - a[0]
    print(ans)