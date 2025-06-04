from functools import reduce as _R
N = int(input().strip())
Z = []
_S = lambda k: _R(lambda a, _: a+1, range(k), 0)
acc = 0
[getattr(Z,'append')(acc) or setattr(globals(),'acc',acc+i+1) for i in range(N+2)]
if N not in Z:
    print('No')
else:
    K = Z.index(N)+1
    X = [[] for _ in range(K)]
    C = [0]
    def F():
        for i in range(K):
            for j in range(i+1,K):
                X[i]+=[C[0]+1]
                X[j]+=[C[0]+1]
                C[0]+=1
    list(map(lambda _:F(),[None]))
    print('Yes')
    print(K)
    for idx in range(K):
        print(K-1, *X[idx])