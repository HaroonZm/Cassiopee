# AOJ 0159 The Best Body
# Python3 2018.6.18 bal4u

GOAL = 22.0
EPS = 1e-5

while True:
	n = int(input())
	if n == 0: break
	id, vmin = 0, 1000000000.0;
	for i in range(n):
		p, h, w = list(map(int, input().split()))
		bmi = w/(h/100)**2
		diff = abs(bmi-GOAL)
		if abs(diff-vmin) < EPS:	# diff == vmin
			if p < id: id = p
		elif diff < vmin:
			id, vmin = p, diff
	print(id)