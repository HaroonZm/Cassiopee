while True:
	try:
		inpt = map(int, raw_input().split())
		print inpt[0] + inpt[1]
	except:
		break