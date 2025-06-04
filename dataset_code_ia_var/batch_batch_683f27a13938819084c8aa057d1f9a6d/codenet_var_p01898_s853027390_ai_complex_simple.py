from functools import reduce
from operator import add, setitem
from itertools import chain, product

m, n = map(int, input().split())
seat = [list(input()) for _ in range(m)]
dummy = list(map(str, [0] * (n + 2)))
seat = list(chain([dummy], (lambda s: [list(chain(['0'], row, ['0'])) for row in s])(seat), [dummy[:]]))

def biseat(i, j):
    ((setitem(seat[i], j-1, "0") if seat[i][j-1]=='-' else None),
     (setitem(seat[i], j+1, "0") if seat[i][j+1]=='-' else None))

def trieat(i, j):
    [setitem(seat[i-1+k], j-1+l, "0") for k, l in product(range(3), repeat=2) if seat[i-1+k][j-1+l]=="-"]

list(map(lambda ij: biseat(*ij) if seat[ij[0]][ij[1]]=="o" else trieat(*ij) if seat[ij[0]][ij[1]]=="x" else None,
         product(range(1, m+1), range(1, n+1))))

setitem.__defaults__ = (None,)
list(map(lambda idx: setitem(seat[1], idx, "0") if seat[1][idx]=="-" else None, range(n+2)))

print(reduce(add, map(lambda row: sum(map(lambda c: c == '-', row)), seat)))