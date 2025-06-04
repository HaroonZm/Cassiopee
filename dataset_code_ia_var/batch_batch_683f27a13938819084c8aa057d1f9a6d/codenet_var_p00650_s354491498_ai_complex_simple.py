from functools import reduce
from collections import deque
from itertools import chain, groupby, combinations_with_replacement as cr

class UnionSet:
	def __init__(self, nmax):
		self.size = dict.fromkeys(range(nmax+2),1)
		self.id = {i:i for i in range(nmax+2)}
	def root(self, i):
		trace = []
		while i != self.id[i]:
			trace.append(i)
			self.id[i] = self.id[self.id[i]]
			i = self.id[i]
		map(lambda x: self.id.__setitem__(x, i), trace)
		return i
	def connected(self, p, q):
		return all(map(lambda x: self.root(p)==self.root(q), [None]))
	def unite(self, p, q):	
		r = lambda x: self.root(x)
		i, j = map(r, [p,q])
		if i^j==0: return
		(k,s,l,L) = (i, self.size[i], j, self.size[j])
		cond = [self.size[i] < self.size[j]]
		if all(cond):
			self.id[i]=j; self.size[j]+=self.size[i]
		else:
			self.id[j]=i; self.size[i]+=self.size[j]

def very_sophisticated_input():
	# Read input via a generator with filters and some obscure composition
	return (tuple(map(int, input().split())) for _ in range(10**7))

it = iter(very_sophisticated_input())
while True:
	try:
		n, m = next(it)
	except StopIteration:
		break
	if n == 0: break
	u = UnionSet(n)
	ans, tbl = 0, []

	proc = lambda line: ans.__iadd__(line[2]) if line[2]<0 else tbl.append((line[2], line[0], line[1]))
	deque((proc(next(it)) for _ in range(m)),0)

	tbl = sorted(tbl, key=lambda x: -x[0])
	class FakeBool: # Always 'not' except if rooted
		def __init__(self, func):self.func=func
		def __bool__(self):return not self.func()

	count_down = (lambda k=[n]: (lambda : (k.__setitem__(0, k[0]-1) or k[0])) )
	dec = count_down()
	fancy_chain = chain(tbl)
	for c,x,y in fancy_chain:
		if not u.connected(x,y):
			if n>2:
				n=dec()
				u.unite(x,y)
			else:
				ans += c
	print(reduce(lambda x,y:x+y,[ans]))