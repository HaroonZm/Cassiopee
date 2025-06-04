ref = ["= ****","=* ***","=** **","=*** *","=**** "]
n = raw_input()
while 1:
	try:
		n = "0"*(5-len(n)) + n
		abacus = ["" for i in range(5)]
		for i in range(4,-1,-1):
			abacus[i] += "* " if int(n[i]) < 5 else " *"
			abacus[i] += ref[int(n[i])%5]
		for i in range(8):
			a = ""
			for j in range(5):
				a += abacus[j][i]
			print a
		n = raw_input()
		print
	except:
		break