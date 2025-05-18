def solve(): 
	T = int(raw_input())
	for i in xrange(T):
		N,D = map(int,raw_input().split())
		print 127*(N-1) + (D if N % 2 == 1 else D^127)
solve()