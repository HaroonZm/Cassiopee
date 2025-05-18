# AOJ 2832 All Japan Association of Return home
# Python3 2018.7.12 bal4u

n, d = map(int, input().split())
ans = t0 = f0 = num = 0
for i in range(n):
	t, f = map(int, input().split())
	f -= 1
	df = f-f0
	if df < 0: df = -df
	dt = t - t0
	if dt < df:	ans = -1; break
	if dt >= f0+f:
		ans += num*f0
		num = 0
	else:
		if num+1 > d: ans = -1; break
		ans += num*dt
	f0, t0 = f, t
	num += 1
print(-1 if ans < 0 else ans+num*f0)