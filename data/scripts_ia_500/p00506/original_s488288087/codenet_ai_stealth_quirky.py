Q = int(input())
V = list(map(lambda x: int(x), input().split()))
M = min(V)+1
print(1)
I = 2
NG = [1]*M

while I < M:
    checker = [1 if V[x] % I != 0 else 0 for x in range(Q)]
    if all(checker):
        print(I)
    else:
        for multiple in range(I, M, I):
            NG[multiple] = 0
    found = False
    for candidate in range(I+1, M):
        if NG[candidate]:
            I = candidate
            found = True
            break
    if not found:
        break