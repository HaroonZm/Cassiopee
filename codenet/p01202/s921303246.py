for i in range(input()):
	step=raw_input().replace("LL","1").replace("UU","1").replace("DD","1").replace("RR","1")
	print "No" if "1" in step else "Yes"