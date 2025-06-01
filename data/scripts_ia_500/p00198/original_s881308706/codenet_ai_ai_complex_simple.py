r = list(map(list, map(lambda x: [0]+list(map(int,x.split(','))), """
0,1,2,3,4,5,6;0,1,3,5,2,4,6;0,1,4,2,5,3,6;0,1,5,4,3,2,6;
0,2,6,3,4,1,5;0,2,3,1,6,4,5;0,2,1,4,3,6,5;0,2,4,6,1,3,5;
0,3,1,2,5,6,4;0,3,2,6,1,5,4;0,3,5,1,6,2,4;0,3,6,5,2,1,4;
0,4,1,5,2,6,3;0,4,2,1,6,5,3;0,4,5,6,1,2,3;0,4,6,2,5,1,3;
0,5,1,3,4,6,2;0,5,3,6,1,4,2;0,5,4,1,6,3,2;0,5,6,4,3,1,2;
0,6,2,4,3,5,1;0,6,3,2,5,4,1;0,6,5,3,4,2,1;0,6,4,5,2,3,1
""".strip().replace('\n','').replace(';','\n').split('\n'))))

from functools import lru_cache
from operator import itemgetter

def same(x, y):
    return any(all(a[x][r_i[j]]==a[y][r_i[j]] for j in range(1,7)) for r_i in r)

def input_generator():
    import sys
    for line in sys.stdin:
        yield line.strip()

gen = input_generator()
next_int = lambda: int(next(gen))
next_line = lambda: next(gen)

while 1:
    n = next_int()
    if n == 0: break
    a = [['']*7 for _ in range(n)]
    flags = [0]*n
    # indirect indexed assignment with mapping
    [(lambda i,s: [a.__setitem__(i, ['']+[*s.split()])])(i, next_line()) for i in range(n)]
    for i in range(n):
        if flags[i]: continue
        for j in range(i+1,n):
            if same(i,j):
                flags[j] = 1
    print(sum(flags))