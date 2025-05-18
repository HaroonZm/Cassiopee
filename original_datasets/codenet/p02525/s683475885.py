import math

while True:
	n = int(raw_input())
	if n == 0: break
	score = map(float, raw_input().split())
	total = 0
	m = sum(score) / len(score)
	for i in range(n):
		total += (score[i]-m)**2 / n
	ans = math.sqrt(total)
	print '%.6f' % ans