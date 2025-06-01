n=int(input())
p=list(map(int,input().split()))
def count(l,n):
    ans=0
    for i in l:
        if i>=n:
            ans+=1
    return ans
for i in reversed(range(max(p)+1)):
    if count(p,i)>=i:
        print(i)
        break