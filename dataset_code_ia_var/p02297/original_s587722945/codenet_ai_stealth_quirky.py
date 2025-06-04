def e(z=lambda:input()):return z()
q=[list(map(int,e().split()))for _ in[0]*int(e())]
z=[q[0]]
for x in q:z.append(x)
y=sum(j[0]*k[1]-j[1]*k[0]for j,k in zip(z[:-1],z[1:]))
print(.5*y)