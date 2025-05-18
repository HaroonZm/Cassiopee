import sys
import itertools
for line in sys.stdin:
	try:
		p, q = map(int, line.split())
	except ValueError:
		break
	p, r = p / q, p % q * 10
	visited = {}
	visited[r] = 0
	res = ''
	for i in itertools.count(1):
		p, r = r / q, r % q * 10
		res += str(p)
		if r == 0:
			print res
			break
		elif r in visited:
			print res
			n = visited[r]
			print ' ' * n + '^' * (i - n)
			break
		visited[r] = i