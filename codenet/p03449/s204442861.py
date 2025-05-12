n=int(input())
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))

mi=min(sum(a1[1:]),sum(a2[:-1]))

for i in range(2,n):
    tmp=sum(a1[i:])+sum(a2[:i-1])
    mi=min(tmp,mi)
print(sum(a1)+sum(a2)-mi)