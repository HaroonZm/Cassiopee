# AOJ 1576: Community Integration
# Python3 2018.7.13 bal4u

# UNION-FIND library
class UnionSet:
	def __init__(self, nmax):
		self.size = [1]*nmax
		self.id = [i for i in range(nmax+1)]
	def root(self, i):
		while i != self.id[i]:
			self.id[i] = self.id[self.id[i]]
			i = self.id[i]
		return i
	def connected(self, p, q): return self.root(p) == self.root(q)
	def unite(self, p, q):
		i, j = self.root(p), self.root(q)
		if i == j: return
		if self.size[i] < self.size[j]:
			self.id[i] = j
			self.size[j] += self.size[i]
		else:
			self.id[j] = i
			self.size[i] += self.size[j]
# UNION-FIND library

N, M = map(int, input().split())
u = UnionSet(N+1)
f = [0]*(N+1)
for i in range(M):
	a, b = map(int, input().split())
	u.unite(a, b)
for i in range(1, N+1): f[u.root(i)] += 1
a = b = 0
for i in range(1, N+1):
	if f[i] == 1: a += 1
	elif f[i] > 1: b += 1
print(abs(a-b))