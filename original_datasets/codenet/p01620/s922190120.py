n2c = dict(zip(range(0,52),"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))
c2n = dict(zip("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",range(0,52)))

def f(c,k):
	return n2c[(c2n[c]-k)%52]

while True:
	kl=int(raw_input())
	if kl==0: break
	ks = map(int, raw_input().split())
	oms = list(raw_input())
	nms = []
	for ki, om in enumerate(oms):
		k = ks[ki%kl]
		nm = f(om,k)
		nms.append(nm)
	print "".join(nms)