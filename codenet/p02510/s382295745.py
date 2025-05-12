while True:
	n = raw_input()
	if n == "-":
		break
	m = (int)(raw_input())
	for i in range(m):
		h = (int)(raw_input())
		n = n[h:] + n[0:h]
	print(n)