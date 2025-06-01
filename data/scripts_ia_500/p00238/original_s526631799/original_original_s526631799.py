import sys
while True:
	t = input()
	if t == 0: sys.exit(0)
	t -= sum(map(lambda x: x[1] - x[0], [map(int, raw_input().split()) for i in xrange(input())]))
	if t <= 0: print "OK"
	else: print t