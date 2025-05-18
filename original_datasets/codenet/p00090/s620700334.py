# AOJ 0090: Overlaps of Seals
# Python3 2018.6.28 bal4u

EPS = 1.0e-8

def crossPoint(p1, p2):
	A = (p1.real-p2.real)/2
	B = (p1.imag-p2.imag)/2
	d = (A*A + B*B)**0.5
	if d*d > 1.0 + EPS: return;
	h = (1 - d*d)**0.5;
	k, X, Y = h/d, (p1.real+p2.real)/2, (p1.imag+p2.imag)/2;
	cross.append(complex(X+k*B, Y-k*A))
	cross.append(complex(X-k*B, Y+k*A))

while True:
	n = int(input())
	if n == 0: break
	circle = [0] * n
	for i in range(n):
		x, y = map(float, input().split(','))
		circle[i] = complex(x, y)
	cross = []
	for i in range(n):
		for j in range(i+1, n):	crossPoint(circle[i], circle[j]);
	ans = 0
	for i in cross:
		f = 0
		for j in circle:
			dx = j.real - i.real
			dy = j.imag - i.imag
			d = dx*dx + dy*dy
			if abs(d-1.0) <= EPS or d <= 1.0: f += 1
		if f > ans: ans = f
	print(1 if ans == 0 else ans)