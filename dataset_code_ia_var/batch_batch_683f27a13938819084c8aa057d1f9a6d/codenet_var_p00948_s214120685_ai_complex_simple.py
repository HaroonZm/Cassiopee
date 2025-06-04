from functools import reduce
from itertools import starmap,repeat,accumulate,chain

exec('''n,m=map(int,input().split())
q=[tuple(map(int,input().split()))for _ in range(m)]
d=dict(enumerate(starmap(lambda x,y:(x,y-1),*zip(*[q]))))
s=sorted(d.items(),key=lambda t:t[1])
x=type('',(),{'a':[i for i in range(n+1)],'b':[i for i in range(n+1)]})()
list(starmap(lambda i,(_,v):(setattr(x.a,v[1],max(x.a[v[1]],x.a[v[1]+1])),setattr(x.b,v[1]+1,min(x.b[v[1]],x.b[v[1]+1]))),enumerate(map(lambda z:z[1],s))))
print(*map(lambda i:x.a[i]-x.b[i]+1,range(n)))
''')