a,b,c,d,e,f=map(int,input().split())
maxsugar=f*e/(100+e)
maxwater=f*100/(100+e)
#print(maxsugar,maxwater)
sugar=[]
for i in range(int(maxsugar)//min(c,d)+2):
    for j in range(int(maxsugar)//min(c,d)+2):
        x=i*c+j*d
        if x<=maxsugar:
            sugar.append(x)
#print(sugar)
water=[]
for i in range(int(maxwater//100+2)//min(a,b)+5):
    for j in range(int(maxwater//100+2)//min(a,b)+5):
        y=i*a+j*b
        water.append(y)
#print(water)
water.remove(0)
ansl=[]
for i in sugar:
    for j in water:
        z=i/(j*100+i)
        xyz=i+j*100
        if xyz<=f and z<=e/(100+e):
            ansl.append((i,j,z))
s,t,r=sorted(ansl,key=lambda x:x[-1])[-1]
print(s+t*100,s)