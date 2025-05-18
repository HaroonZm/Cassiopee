# AOJ 0135 Clock Short Hand and Long Hand
# Python3 2018.6.18 bal4u

for _ in range(int(input())):
	h, m = list(map(int, input().split(':')))
	H, M = (30*h+(m//2))*2, (6*m)*2
	if (m & 1) == 1: H += 1
	a = H-M
	if a < 0: a = -a
	a2 = 720-a
	if a2 < a: a = a2
	if a < 60: print("alert")
	elif a >= 180 and a <= 360: print("safe")
	else: print("warning")