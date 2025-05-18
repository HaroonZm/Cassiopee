a,b,c,n=map(int,input().split())
x=[0]*n;y=[0]*n;z=[0]*n;s=0
for i in range(n):
    x[i],y[i],z[i]=map(int,input().split())
    s+=(x[i]==a-1)+(y[i]==b-1)+(z[i]==c-1)+(x[i]==0)+(y[i]==0)+(z[i]==0)
for i in range(n):
    for j in range(i+1,n):s+=((abs(x[i]-x[j])+abs(y[i]-y[j])+abs(z[i]-z[j]))==1)
print(2*((a*b+b*c+c*a)+3*n-s))