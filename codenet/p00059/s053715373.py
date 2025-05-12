import sys

for line in sys.stdin:
    xa1, ya1, xa2, ya2, xb1, yb1, xb2, yb2 = map(float, line.strip().split(' '))
    if ((xb1<=xa1 and xa1<=xb2) or (xa1<=xb1 and xb1<=xa2)) and ((yb1<=ya2 and ya2<=yb2) or (ya1<=yb2 and yb2<=ya2)):
        print 'YES'
    else:
        print 'NO'