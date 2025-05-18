num=input()
a=[]
for i in range(num):
    p=input()
    a.append(p)
ans=a[0]-1
a.pop(0)
nowprice=2
for custom in a:
    if (custom>nowprice):
        if custom % (nowprice)==0:
            ans += custom / (nowprice )-1
        else:
            ans+=custom/(nowprice)
    if (custom==nowprice):
        nowprice+=1
print ans