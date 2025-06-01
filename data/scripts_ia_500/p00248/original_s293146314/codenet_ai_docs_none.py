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

while True:
	n, m = map(int, input().split())
	if n == 0: break
	n += 1
	u = UnionSet(n)
	f = [0]*n
	ans = True
	for i in range(m):
		if ans:
			a, b = map(int, input().split())
			f[a] += 1
			f[b] += 1
			if f[a] > 2: ans = False
			if f[b] > 2: ans = False
			if u.connected(a, b): ans = False
			u.unite(a, b)
		else: input()
	print("yes" if ans else "no")