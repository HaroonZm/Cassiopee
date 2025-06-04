n=input()
res=10**18
l=len(n)
for length in range(1,l):
    max_v=-1
    min_v=10**18
    i=0
    while i<l:
        val=int(n[i:i+length])
        max_v=max(max_v,val)
        min_v=min(min_v,val)
        i+=length
    res=min(res,max_v-min_v)
print(res)