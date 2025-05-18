p=[1 for i in range(1000001)]
p[0]=0
p[1]=0
for i in range(2,500000):
    for j in range(2,1000000//i+1):
        p[i*j]=0

while True:
    n=int(input())
    if n==0:
        break
    s=0
    for i in range(1,n//2+1):
        if p[i]==1 and p[n-i]==1:
            s+=1
    print(s)