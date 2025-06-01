d=dict()
exec("a,b=input().split();d[a]=d.get(a,0)+int(b);"*int(input()))
keys=sorted(d,key=lambda x:(len(x),x))
for key in keys:print(key,d[key])