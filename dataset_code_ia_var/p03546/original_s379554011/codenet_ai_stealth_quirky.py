# Début de code avec quelques choix de style non-standards

_=_=lambda:map(int,input().split())
H,W= _()
C= [list(_()) for _0 in range(10)]
[[[C[i].__setitem__(j, min(C[i][j], C[i][k]+C[k][j])) for k in range(10)] for j in range(10)] for i in range(10)]
for _magic in (lambda x:[9-x for x in range(10)], lambda x:range(10)):
    for i in range(10):
        for j in range(10):
            for k in _magic(0):
                C[i][j]=min(C[i][j],C[i][k]+C[k][j])
l_ = sum([[*_( )] for __ in range(H)],[])
print(sum(C[i][1]*l_.count(i) for i in range(10)))