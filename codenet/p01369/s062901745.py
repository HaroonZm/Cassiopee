R = "yuiophjklnm"
def tf(a):
	return 1 if a in R else 0
while 1:
	s = raw_input()
	if s == "#": break
	print sum([abs(tf(s[i-1])-tf(s[i])) for i in range(1,len(s))])