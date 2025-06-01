def f(a):
	ans = ""
	s = a[0]
	c = 1
	for i in range(1,len(a)):
		if a[i] == s:
			c += 1
		else:
			ans += str(c) + s
			s = a[i]
			c = 1
	ans += str(c) + s
	return ans
	
while 1:
	n = input()
	if n == 0: break
	a = raw_input()
	for i in range(n):
		a = f(a)
	print a