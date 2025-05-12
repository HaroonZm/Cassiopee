for i in range(input()):
	step=raw_input()
	flag=0
	for j in range(len(step)-1):
		if step[j]==step[j+1]:
			print "No"
			break
	else:
		print "Yes"