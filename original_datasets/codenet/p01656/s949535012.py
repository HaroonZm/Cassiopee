import sys
readline = sys.stdin.readline

N, Q = (int(x) for x in readline().split())
name = "kogakubu10gokan"
for i in xrange(N):
    y, n = readline().split()
    if int(y) <= Q:
        name = n
print name