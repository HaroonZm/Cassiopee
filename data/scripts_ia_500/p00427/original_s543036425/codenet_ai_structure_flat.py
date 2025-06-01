from decimal import *
while True:
	n, k, m, r = map(int, input().split())
	if n == 0:
		break
	setcontext(Context(prec=r, rounding=ROUND_HALF_UP))
	one = Decimal(1)
	ans = one / Decimal(n)
	if m == 1:
		s = 0
		for i in range(1, n):
			s += one / Decimal(i)
		ans = ans * (1 + s)
	ans = str(ans)
	if len(ans) < r + 2:
		ans += '0' * (r + 2 - len(ans))
	else:
		ans = ans[:r+2]
	print(ans)