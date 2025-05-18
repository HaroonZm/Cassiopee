d={}
for _ in[0]*int(input()):
 k,v=input().split()
 d[k]=d.get(k,0)+int(v)
for k in sorted(d,key=lambda x:(sum(27**i*(ord(k)-64)for i,k in enumerate(x[::-1])),x)):
 print(k,d[k])