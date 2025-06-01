import sys
fe = ["A","B","C"]
for line in sys.stdin:
	num = line[:-1].split(",")
	if num[0] == "A":
		if num[1] == "B":
			tako = fe[0]
			fe[0] = fe[1]
			fe[1] = tako
		else:
			tako = fe[0]
			fe[0] = fe[2]
			fe[2] = tako

	elif num[0] == "B":
		if num[1] == "A":
			tako = fe[1]
			fe[1] = fe[0]
			fe[0] = tako
		else:
			tako = fe[1]
			fe[1] = fe[2]
			fe[2] = tako

	elif num[0] == "C":
		if num[1] == "A":
			tako = fe[0]
			fe[0] = fe[2]
			fe[2] = tako
		else:
			tako = fe[1]
			fe[1] = fe[2]
			fe[2] = tako
		
if fe.index("A") == 0: print "A"
elif fe.index("A") == 1: print "B"
else:	print "C"