l = []
while 1 :
	c = raw_input().split()
	if c[0] == "push" : l.append(c[1])
	elif c[0] == "pop" : print l.pop()
	elif c[0] == "quit" : break