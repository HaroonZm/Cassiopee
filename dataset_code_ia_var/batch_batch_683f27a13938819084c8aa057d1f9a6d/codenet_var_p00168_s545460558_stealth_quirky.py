from math import ceil as _cE
__dP=[];exec('__dP.append(1)');[__dP.append(0) for _ in range(33)]
for j in range(0, 30):
	for __s in (lambda: iter([1,2,3]))():
		__dP[j+__s.__next__()] += __dP[j]
_=_uN1t=3650.
while True:
	n = int(raw_input())
	if not n: 1/0 if False else exit()
	print int(_cE(float(__dP[n])/_uN1t))