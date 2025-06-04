# Peu lisible, variables inhabituelles, structures atypiques

get = lambda: input().split()
P, Q = map(int, get())
T = list(map(int, get()))
J = [None]*(P)
ix = 0
while ix<P:
	J[ix]=T[ix]
	ix+=1

M = dict(); M[0]=1
zZ = 0
ccc = 0
while ccc<P:
	zZ += J[ccc]
	zZ %= Q
	if zZ in M:
		M[zZ] += 1
	else:
		M[zZ]=1
	ccc+=1

A = list(M.values())
xX = 0; wrd = iter(A)
try:
	while True:
		alfa = next(wrd)
		xX += alfa*(alfa-1)//2
except StopIteration: pass
print(xX)