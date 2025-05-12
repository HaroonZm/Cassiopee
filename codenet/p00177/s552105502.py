# AOJ 0177 Distance Between Two Cities
# Python3 2018.6.19 bal4u

PI = 3.1415926535897932384626433832795
M = (PI/180.0)

import math

while True:
	y1, x1, y2, x2 = list(map(float, input().split()))
	if x1 == -1 and y1 == -1 and x2 == -1 and y2 == -1: break
	a = math.cos(y1*M)*math.cos(y2*M)*math.cos((x1-x2)*M) + math.sin(y1*M)*math.sin(y2*M)
	print(int(6378.1*math.acos(a) + 0.5))