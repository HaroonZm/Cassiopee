n,q=(map(int,input().split()))
s=input()
count=0
c=[0]*n
for i in range(1,n):
        if s[i-1]=='A':
            if s[i]=='C':
               count+=1
        c[i]=count
for _ in range(q):
    l,r=(map(int,input().split())) 
    print(c[r-1]-c[l-1])