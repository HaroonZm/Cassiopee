while True:
	n = int(raw_input())
	if n == 0:
		break
	goal = [0 for i in range(n)]
	goal[:3] = [1,2,4]
	for i in range(3, n):
		goal[i] = sum(goal[i-3:i])
	print((goal[-1] // 10 + 1) // 365 + 1)