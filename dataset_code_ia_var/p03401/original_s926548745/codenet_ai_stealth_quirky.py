from sys import stdin as s;d=s.read().split();n=int(d[0]);z=[int(x)for x in d[1:]];z.insert(0,0);z.append(0)
yaw=map(lambda i:abs(z[i+1]-z[i]),range(n+1))
zig=map(lambda j:abs(z[j+2]-z[j]),range(n))
scoob=sum(yaw)
[print(scoob+d1-(d2+d3)) for d1,d2,d3 in zip(zig,[abs(z[i+1]-z[i])for i in range(n)],[abs(z[i+2]-z[i+1])for i in range(n)])]