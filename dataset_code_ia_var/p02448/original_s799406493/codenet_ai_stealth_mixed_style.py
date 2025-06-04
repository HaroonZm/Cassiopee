import sys

def _inp():
    return sys.stdin.readline()

n = int(_inp())
p = []
for _ in range(n):
    tmp = _inp().split()
    p.append([int(tmp[0]),int(tmp[1]),tmp[2],int(tmp[3]),tmp[4]])

def srt(l):
    arr = list(l)
    arr.sort()
    return arr

out = srt(p)

for e in out:
    print("{0} {1} {2} {3} {4}".format(*e), file=sys.stdout)