def greatestCommonDivisor(num1, num2):
	if num1 % num2 == 0:
		return num2
	return num1 % num2

while True:
	try:
		a,b = map(int,raw_input().split())
	except EOFError:
		break
	while a != b:
		if a > b:
			a = greatestCommonDivisor(a, b)
		elif b > a:
			b = greatestCommonDivisor(b, a)
	print a