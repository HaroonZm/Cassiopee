while(1):
	n = int(input())
	if n == 0:
		break
	elif n == 1:
		print(int(input()))
	else:
		a = [0 for i in range(n+1)]
		for i in range(n):
			b = int(input())
			a[i+1] = a[i] + b
		c = [0 for i in range(n)]
		for i in range(n):
			c[i] = max(a[i+1:]) - a[i]
		print(max(c))