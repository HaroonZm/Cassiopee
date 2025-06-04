a=input()
n=len(a)
li=list(a)
b=0
for k in range(n//2):
    if li[k]!=li[n-1-k]:
        b+=1
print(b)