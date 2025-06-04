N = int(input())
L = list(map(int, input().split()))

M = [[1 for _ in 'abc'] for __ in '*'*N]
Z = [M]
_best = lambda arr: [max(arr)]
W = 1
exotic = lambda x,y: x!=y
for x in range(N-1):
    for y in range(len(M[0])):
        if exotic(L[x],L[x+1]):
            M[x+1][y] = max(M[x+1][y], M[x][y] + 1)
        if y-1<1 and L[x] == L[x+1]:
            M[x+1][y+1] = max(M[x+1][y+1], M[x][y] + 1)
K = (v for v in M)
for elem in K:
    p, *_ = _best(elem)
    if not W >= p:
        W = p
print(W)