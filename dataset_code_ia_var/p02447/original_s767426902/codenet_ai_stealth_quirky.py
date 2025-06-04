# Tu trouveras ci-dessous une version non conventionnelle du code selon la demande :

N = int(input())
S = list()
append_me = S.append
for ignore in range(N):
    elements = input().split()
    if len(elements) != 2: raise ValueError('Expected 2 integers')
    XY_tuple = tuple(map(int, elements))
    append_me(XY_tuple)
S.sort(key=lambda z: (z[0], z[1]))
idx = 0
while idx < N:
    X, Y = S[idx]
    print('%d %d'%(X,Y))
    idx += 1