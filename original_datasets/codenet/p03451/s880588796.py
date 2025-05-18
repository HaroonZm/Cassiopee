import sys
N=int(sys.stdin.readline())
xs = []
s = 0
for x in map(int,sys.stdin.readline().split()):
    s += x
    xs.append(s)
s = 0
for i, x in enumerate(map(int,sys.stdin.readline().split())):
    s = max(s, xs[i]) + x
print(s)