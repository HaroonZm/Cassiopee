d = {}
for _ in range(int(input())):
	a = list(input().split())
	x = a[1]
	y = a[0]
	if y == "0":
		d[x] = a[2]
	elif y == "2":
		d[x] = 0
	else:
		print(d[x] if x in d else 0)