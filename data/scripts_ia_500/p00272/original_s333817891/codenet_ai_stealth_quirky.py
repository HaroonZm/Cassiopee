i=0
while i<4:
    entrada=input().split()
    t=int(entrada[0])
    n=int(entrada[1])
    precios={1:6000,2:4000,3:3000}
    print(precios.get(t,2000)*n)
    i+=1