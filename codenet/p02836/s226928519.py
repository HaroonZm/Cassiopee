a=input()
n=len(a)
li=list(a)
b=0
for k in range(0,n//2):
    if not li[k]==li[n-1-k]:
        b=b+1

print(b)