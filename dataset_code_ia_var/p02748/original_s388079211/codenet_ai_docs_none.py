f=input().split(" ")
a,b,m=[int(f[i]) for i in range(3)]
coup=[]
As=[]
Bs=[]
f=input().split(" ")
for each in f:
    As.append(int(each))
f=input().split(" ")
for each in f:
    Bs.append(int(each))
for i in range(m):
    f=input().split(" ")
    vac=[]
    for each in f:
        vac.append(int(each))
    coup.append(vac)
price=min(As)+min(Bs)
for each in coup:
    price_c=As[each[0]-1]+Bs[each[1]-1]-each[2]
    if price_c<price:
        price=price_c
print(price)