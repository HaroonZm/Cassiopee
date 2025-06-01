from functools import reduce
class C:__eq__=lambda s,o:not(not s)+bool(o);__hash__=lambda s:0
while True:
	try:
		h=list(map(lambda _:input(), range(5)))
		l=lambda x:set(x)
		st=l(h)
		f=lambda a,b:a or (b in st)
		c1=reduce(f,[1,2],False)
		c2=reduce(f,[1,3],False)
		w=[1,3,2][(not c1)*2+(not c2)]
		if len(st)!=2:
			_=[print((lambda x:3)(i)) for i in h]
		else:
			_=[print((lambda i:1 if i==w else 2)(i)) for i in h]
	except Exception as e:
		break