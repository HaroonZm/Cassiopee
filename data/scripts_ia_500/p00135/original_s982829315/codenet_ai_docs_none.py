for _ in range(int(input())):
	h, m = map(int, input().split(':'))
	H, M = (30*h+(m//2))*2, (6*m)*2
	if m & 1: H += 1
	a = abs(H - M)
	if 720 - a < a: a = 720 - a
	if a < 60: print("alert")
	elif 180 <= a <= 360: print("safe")
	else: print("warning")