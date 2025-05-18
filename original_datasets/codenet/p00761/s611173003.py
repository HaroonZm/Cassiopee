while True:
	a, l = map(int, input().split())
	if (a, l) == (0, 0):
		break

	arr = [a]
	for i in range(20):
		p = list(map(int, '{0:0>{1}}'.format(a, l)))
		a = int(''.join(map(str,sorted(p, reverse=True)))) - int(''.join(map(str,sorted(p))))
		if a in arr:
			break
		arr.append(a)

	j = arr.index(a)
	print('{} {} {}'.format(j, a, len(arr)-j))