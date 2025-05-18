r = "abcdefghijklmnopqrstuvwxyz"
while 1:
	n = input()
	if n == 0: break
	s = list(raw_input())
	ab = [map(int,raw_input().split()) for i in range(n)]
	for a,b in ab[::-1]:
		d = abs(a - b)
		s[a-1],s[b-1] = r[(r.index(s[b-1]) + d)%26],r[(r.index(s[a-1]) + d)%26]
	print "".join(s)