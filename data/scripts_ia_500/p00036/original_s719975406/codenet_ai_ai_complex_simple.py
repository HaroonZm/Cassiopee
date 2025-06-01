from functools import reduce
ans = list(map(chr, map(lambda x: x+65, range(7))))
def get(x):
    def check(conds):
        return all((x[i][j] == '1') for i,j in conds)
    coords = [(i, j) for i in range(8) for j in range(8)]
    def cases():
        for i, j in coords:
            if i<7 and j<7 and check([(i,j),(i+1,j),(i,j+1),(i+1,j+1)]): yield 0
            if i<5 and check([(i,j),(i+1,j),(i+2,j),(i+3,j)]): yield 1
            if j<5 and check([(i,j),(i,j+1),(i,j+2),(i,j+3)]): yield 2
            if i<6 and j>0 and check([(i,j),(i+1,j),(i+1,j-1),(i+2,j-1)]): yield 3
            if i<7 and j<6 and check([(i,j),(i,j+1),(i+1,j+1),(i+1,j+2)]): yield 4
            if i<6 and j<7 and check([(i,j),(i+1,j),(i+1,j+1),(i+2,j+1)]): yield 5
            if i<7 and 0<j<7 and check([(i,j),(i,j+1),(i+1,j),(i+1,j-1)]): yield 6
    return next(cases(), None)
from sys import stdin
readline = (lambda f=stdin.readline: lambda: f().rstrip('\n'))()
while True:
    try:
        l = [readline() for _ in range(8)]
        print(ans[get(l)])
        readline()
    except:
        break