# AOJ 1078: SAT-EN-3
# Python3 2018.7.10 bal4u

def clause(e):
	f = True
	dic = {}
	f = e.split('&')
	for x in f:
		pm, t = 1, x[0]
		if t == '~':
			pm, t = -1, x[1]
		if t in dic and dic[t] + pm == 0: f = False
		dic[t] = pm
	return f

while True:
	p = input()
	if p == '#': break
	exp = list(p.split('|'))
	ans = False
	for e in exp:
		if clause(e[1:-1]):
			ans = True
			break
	print("yes" if ans else "no")