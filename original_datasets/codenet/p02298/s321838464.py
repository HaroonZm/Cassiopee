n = input()
p = [map(int, raw_input().split()) for i in xrange(n)]
for i in xrange(n):
    x1 = p[i-1][0] - p[i-2][0]
    y1 = p[i-1][1] - p[i-2][1]
    x2 = p[i][0] - p[i-2][0]
    y2 = p[i][1] - p[i-2][1]
    if x1*y2 - y1*x2 < 0:
        print 0
        break
else:
    print 1