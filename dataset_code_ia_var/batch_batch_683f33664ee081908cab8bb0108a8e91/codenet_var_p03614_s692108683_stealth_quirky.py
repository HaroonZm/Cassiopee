z=int(input())
x=[*map(int,input().split())]
y={i:0 for i in range(z)}
w=lambda a,b:a==b-1
for u in range(z):
    if w(u,x[u]):
        y[u]=True
    if u and y[u-1]&y[u]:
        y[u]=False
print(sum(1 for k in y if y[k]))