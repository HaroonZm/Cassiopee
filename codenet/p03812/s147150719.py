n=int(input());a=list(map(int,input().split()));e=[[]for _ in[0]*n]
for x,y in[map(int,input().split())for _ in[0]*(n-1)]:e[x-1].append(y-1);e[y-1].append(x-1)
def b(r,v):return sum((r!=i)and(a[v]>a[i])and(not(b(v,i)))for i in e[v])
print(*[i+1for i in range(n)if b(n,i)])