tp = {}
while 1:
	t,p = map(int,raw_input().split(","))
	if t == p == 0: break
	tp[t] = p
plist = sorted(list(set([tp[key] for key in tp.keys()])),reverse = True)
while 1:
	try:
		team = int(raw_input())
	except:
		break
	print plist.index(tp[team])+1