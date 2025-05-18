a=raw_input().split()
dawa=''
d={}
for w in a:
	if len(w)>len(dawa): dawa=w
	d[a.count(w)]=w
m=max(d.keys())
akeh=d.get(m)
print '%s %s' % (akeh,dawa)