n = input()
i = 0
while 1:
	n1,n2 = str(n-i), str(n+i)
	if n1 == n1[::-1]:
		print n1
		break
	elif n2 == n2[::-1]:
		print n2
		break
	i += 1