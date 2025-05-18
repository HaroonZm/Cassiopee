def read():
    return(list(map(float,input().split(","))))
def triArea(va,vb,vc):
    return(abs((va[0]-vc[0])*(vb[1]-vc[1])-(va[1]-vc[1])*(vb[0]-vc[0]))/2)
v1=read()
va=read()
vb=read()
s=triArea(v1,va,vb)
while 1:
    try:
        va=vb
        vb=read()
        s+=triArea(v1,va,vb)
    except:break
print(s)