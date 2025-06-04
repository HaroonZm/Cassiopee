i=0
while not (i==3):
	x,y,z,p,q,r=[*map(int,input().split())]
	lambda a,b,c,d,e,f:print(str((3600*(d-a)+60*(e-b)+(f-c))//3600)+' '+str((3600*(d-a)+60*(e-b)+(f-c))%3600//60)+' '+str((3600*(d-a)+60*(e-b)+(f-c))%3600%60))\
	(x,y,z,p,q,r)
	i+=1