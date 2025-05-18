# AOJ 1053: Accelerated Railgun
# Python3 2018.7.7 bal4u

EPS = 1e-7
while True:
	d = float(input())
	if d == 0: break
	px, py, vx, vy = map(float, input().split())
	ans = d+1
	dp = (px*px + py*py)**0.5
	dv = (vx*vx + vy*vy)**0.5
	x = (px*vx + py*vy)/(dp*dv)
	if abs(x+1) <= EPS: ans = dp
	elif abs(1-x) <= EPS: ans = 2-dp
	print(ans if abs(ans-d) <= EPS or ans <= d else "impossible")