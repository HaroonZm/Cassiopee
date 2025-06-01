while True:
	try:
		a = list(input())
		for koma in ['o', 'x']:
			win = False
			for i in range(3):
				if a[i] == koma and a[i+3] == koma and a[i+6] == koma:
					print(koma)
					win = True
					break
				if a[3*i] == koma and a[3*i+1] == koma and a[3*i+2] == koma:
					print(koma)
					win = True
					break
			if win:
				break
			if not win and ((a[0] == koma and a[4] == koma and a[8] == koma) or (a[2] == koma and a[4] == koma and a[6] == koma)):
				print(koma)
				win = True
				break
		if not win:
			print('d')
	except EOFError:
		break