while 1:
	ls = raw_input()
	if ls == "-" : break
	
	h = 0
	for i in range(int(raw_input())):
		h += int(raw_input())
	h %= len(ls)
	print ls[h:] + ls[:h]