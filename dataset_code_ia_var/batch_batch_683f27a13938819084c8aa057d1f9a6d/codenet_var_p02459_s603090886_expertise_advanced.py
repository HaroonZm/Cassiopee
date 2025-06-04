from sys import stdin
from operator import setitem, itemgetter

d = {}
ops = {'0': lambda x, y: setitem(d, x, int(y)), '1': lambda x: print(d[x])}

for _ in range(int(stdin.readline())):
    cmd, *args = stdin.readline().split()
    ops[cmd](*args)