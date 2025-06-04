while 1:
	b, r, g, c, s, t = map(int, input().split())
	if (b|r|g|c|s|t) == 0: break
	ans = 100
	ans += 15*b + 65*b
	t -= 5*b
	ans += 15*r + 39*r
	t -= 3*r
	ans += 7*g
	ans += 2*c
	t -= s
	ans -= 3*t
	print(ans)