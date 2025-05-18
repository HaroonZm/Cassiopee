# AOJ 0520: Lightest Mobile
# Python3 2018.6.30 bal4u

def lcm(a, b):
	return a // gcd(a, b) * b

def gcd(a, b):
	while b != 0:
		r = a % b
		a, b = b, r
	return a

def calc(i):
	wr = calc(t[i][2]) if t[i][2] > 0 else 1
	wb = calc(t[i][3]) if t[i][3] > 0 else 1
	w = lcm(t[i][0] * wr, t[i][1] * wb)
	return w//t[i][0] + w//t[i][1]

while True:
	n = int(input())
	if n == 0: break
	f = [0]*(n+1)
	t = [(0,0,0,0)]
	for i in range(1, n+1):
		p, q, r, b = map(int, input().split())
		t.append((p, q, r, b))
		if r > 0: f[r] = i
		if b > 0: f[b] = i
	for i in range(1, n+1):
		if f[i] == 0: break
	print(calc(i))