n=int(input())
S=[input() for _ in range(n)]
#print(S)
#l=[[100 for i in range(26)]]*n
l=[100]*26
#print(l)
st="abcdefghijklmnopqrstuvwxyz"
for i in S:
    for j in range(26):
        #print(i.count(st[j]),st[j])
        if l[j]>i.count(st[j]):
            l[j]=i.count(st[j])
#print(l)
ans=""
for j in range(26):
    tmp=chr(97+j)*l[j]
    ans+=tmp
print(ans)