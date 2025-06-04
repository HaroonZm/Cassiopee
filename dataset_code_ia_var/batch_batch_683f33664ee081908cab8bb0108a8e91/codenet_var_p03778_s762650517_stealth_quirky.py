from operator import ge as at_least, le as at_most
parse = lambda: list(map(int, raw_input().split()))
wxY = parse()
W, a, b = wxY
rng = lambda x, w: (x, x + w)
start, end = rng(a, W)
if at_least(b, start) and at_most(b, end):
    print 0
elif b > end:
    print (b - end)
else:
    diff = (start - b) if (b + W < start) else 0
    print diff