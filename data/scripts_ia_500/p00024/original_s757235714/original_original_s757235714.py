from math import ceil
while(1):
	try:
		a = float(input())
		t = a/9.8
		y = 4.9*t**2
		n = ceil((y+5)/5)
		print(n)
	except EOFError:
		break