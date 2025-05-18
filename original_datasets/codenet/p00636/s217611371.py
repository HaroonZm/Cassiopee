# AOJ 1050 The Last Dungeon
# Python3 2018.7.7 bal4u

import math
import heapq

EPS = 1e-8
pp0 = [0j, 4+0j, 4+4j, 4j]

def EQ(a,b): return abs(a-b)<EPS
def PPeQ(a,b): return EQ(a.real, b.real) and EQ(a.imag, b.imag)
def dcmp(x):
	if PPeQ(x, 0): return 0
	return -1 if x <= 0 else 1
def cross(a, b): return a.real*b.imag - a.imag*b.real
def vabs(a): return math.hypot(a.real, a.imag)

# ２線分間の交点 (SEG a, PP bs, PP be)
def crossPointS2P(seg, bs, be):
	a1 = cross(be-bs, seg[0]-bs)
	a2 = cross(be-bs, seg[1]-bs)
	return complex((seg[0].real*a2-seg[1].real*a1)/(a2-a1),	(seg[0].imag*a2-seg[1].imag*a1)/(a2-a1))

# 垂直二等分線 (PP a, PP b)
def bisector(a, b):
	ax, ay = (a.real + b.real)/2, (a.imag + b.imag)/2
	if EQ(a.imag, b.imag): return [complex(ax, ay), complex(ax, ay+(b.real-a.real)*100)]
	t = ax-(b.imag-a.imag)*100
	return [complex(ax, ay), complex(t, (ax-t)*(b.real-a.real)/(b.imag-a.imag)+ay)]

# 凸包を直線で切断して左側を残す (SEG a, PP *p)
def convex_cut(seg, p):
	ans, n = [], len(p)
	for i in range(n):
		d1 = dcmp(cross(seg[1]-seg[0], p[i]-seg[0]))
		t = p[0] if i+1 == n else p[i+1]
		d2 = dcmp(cross(seg[1]-seg[0], t-seg[0]))
		if d1 >= 0: ans.append(p[i])
		if d1*d2 < 0: ans.append(crossPointS2P(seg, p[i], t))
	return ans

def pushBack(a, b):
	if EQ(tbl[a].imag, 0) and EQ(tbl[b].imag, 0): return
	if EQ(tbl[a].imag, 4) and EQ(tbl[b].imag, 4): return
	if b in to[a]: return;
	to[a].append(b)

def dijkstra(V, to, tbl):
	visited = [0]*V
	Q = []
	for i in range(V):
		if EQ(tbl[i].real, 0):
			heapq.heappush(Q, (0, i, 0))
			visited[i] = 1
	while Q:
		t, s, x	= heapq.heappop(Q)
		if EQ(x, 4): return t
		for e in to[s]:
			if visited[e]: continue
			visited[e] = 1
			heapq.heappush(Q, (t+vabs(tbl[s]-tbl[e]), e, tbl[e].real))
	return -1

while True:
	n = int(input())
	if n == 0: break
	p = []
	for i in range(n):
		x, y = map(float, input().split())
		p.append(complex(x, y))
	if n == 1:
		print("impossible")
		continue;
	tbl, sz = [], 0
	to = [[] for i in range(50)]
	for i in range(n):
		po = pp0[0:]
		for j in range(n):
			if j == i: continue
			seg = bisector(p[i], p[j])
			po = convex_cut(seg, po)
		w = len(po)
		if w <= 1: continue
		if w == 2:
			a, sz = sz, sz+1
			tbl.append(po[0])
			b, sz = sz, sz+1
			tbl.append(po[1])
			pushBack(a, b)
			pushBack(b, a)
		else:			# k >= 3
			j = sz		# j as memo
			sz += w
			tbl.extend(po)
			a, c = w-1, 1
			for b in range(w):
				pushBack(j+b, j+a)
				pushBack(j+b, j+c)
				a, c = a+1, c+1
				if a == w: a = 0
				if c == w: c = 0
	for i in range(sz):
		for j in range(i+1, sz):
			if PPeQ(tbl[i], tbl[j]):
				pushBack(i, j)
				pushBack(j, i)
	ans = dijkstra(sz, to, tbl)
	print("impossible" if ans < 0 else ans)