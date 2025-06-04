import sys as __s
___________ = lambda: map(int, __s.stdin.readline().split())
___, ____ = ___________()
OOOoooOOooO = [list(__s.stdin.readline().strip()) for _ in range(___)]
___O = sum(row.count('.') for row in OOOoooOOooO)
_𝓎_ = 999999999
ooooOOOO = [[_𝓎_]*____ for _ in range(___)]
__dx, __dy = (-1,0,1,0), (0,1,0,-1)
ooooOOOO[0][0] = 0
q = []
(q.append([0,0]),)
while q:
    Xy = q.pop(0)
    if Xy == [____-1, ___-1]: break
    for i in range(4):
        __X, __Y = Xy[0]+__dx[i], Xy[1]+__dy[i]
        if 0<=__X<____ and 0<=__Y<___ and OOOoooOOooO[__Y][__X] == '.' and ooooOOOO[__Y][__X]==_𝓎_:
            ooooOOOO[__Y][__X]=ooooOOOO[Xy[1]][Xy[0]]+1
            (q.append([__X,__Y]),)
if ooooOOOO[___-1][____-1]==_𝓎_:
    print(~0)
else:
    print(___O - ooooOOOO[___-1][____-1] - 1)