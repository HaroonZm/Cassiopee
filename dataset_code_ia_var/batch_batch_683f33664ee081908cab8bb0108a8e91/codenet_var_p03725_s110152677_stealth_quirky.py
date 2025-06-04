import sys as __s
_q = lambda: list(map(int, __s.stdin.readline().split()))
_H, _W, _K = _q()
_M = []
Best_o_o = 1<<60
for _ii in range(_H):
    L = __s.stdin.readline().strip()
    _M += [L]
    for _jj, z in enumerate(L):
        if z == 'S': _S = (_ii, _jj)
N = [[Best_o_o]*_W for _ in range(_H)]
N[_S[0]][_S[1]] = 0
B = [_S]
_X = (0, -1, 0, 1)
_Y = (-1, 0, 1, 0)
while B:
    a,b = B.pop(0)
    Best_o_o = min(Best_o_o, 2+(min(a,b,_H-a-1,_W-b-1)-1)//_K)
    for z in range(4):
        w,v = a+_X[z], b+_Y[z]
        if 0<=w<_H and 0<=v<_W and _M[w][v]=='.' and N[w][v]==1<<60:
            N[w][v]=N[a][b]+1
            if N[w][v]<=_K: B.append((w,v))
print(Best_o_o)