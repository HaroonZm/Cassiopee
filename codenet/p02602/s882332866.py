n,k=map(int,input().split())
l=list(map(int,input().split()))
pr=1
t=[]
for i in range(len(l)-k):
    if l[i]<l[i+k]:
        print("Yes")
    else:
        print("No")