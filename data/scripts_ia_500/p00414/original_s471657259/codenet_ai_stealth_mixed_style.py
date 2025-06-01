l,n=map(int,input().split())
s=input()
c=0
i=0
while i < l-1:
    if s[i:i+2]=="oo":
        c+=1
    i+=1
def double_count(x):
    return x*2
for _ in range(n):
    l = l + c*3
    c = double_count(c)
print(l)