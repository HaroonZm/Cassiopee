from functools import reduce
t,b = map(str,(lambda x:(x(),x()))(input))
f = lambda x,y:x+[y]
g = lambda q,r,s,t,u,v,w,x,y,z: z if y else g(q,r,s,t,u,v,w,x,y-1,z) if r[s] != t[y] else (g(q,r,s,t,u,v,w,x,y-1,z)+q[u-1][y-1])%1000000007
table = [[0]*len(t) for _ in b]
if len(t)>len(b):
    table[0][0] = int(t[0]==b[0])
    list(map(lambda i: table[0].__setitem__(i,table[0][i-1]+int(t[i]==b[0])), range(1,len(t))))
    def h(i):
        if b[i]==t[i]: table[i][i]=table[i-1][i-1]
        for j in range(i+1,len(t)):
            table[i][j] = (table[i][j-1] + (table[i-1][j-1] if b[i]==t[j] else 0)) % 1000000007
    list(map(h, range(1,len(b))))
    print(table[-1][-1]%1000000007)
elif len(t)==len(b):
    print(int(t==b))
else:
    print(0)