n = int(raw_input())
a = []
for i in xrange(n):
    line = raw_input().split()
    a.append(map(int, line))

def rotate_point(p):
    return (-p[1], p[0])

a = [rotate_point(p) for p in a]
a.sort()
print a[0][1], -a[0][0]