while 1:
	n = input()
	if n == 0: break
	ans = []
	for i in range(n):
		inp = raw_input().split()
		P,A,B,C,D,E,F,S,M = map(int,inp[1:])
		ans.append([inp[0],(M*F*S-P)*1.0/(A+B+C+(D+E)*M)])
	ans = sorted(sorted(ans), key = lambda x:x[1], reverse = True)
	for k,v in ans: print k
	print "#"