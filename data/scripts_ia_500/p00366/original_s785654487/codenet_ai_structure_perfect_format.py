n=int(input())
max_t=0
timing=[]
for i in range(n):
    timing.append(int(input()))
    if timing[i]>max_t:
        max_t=timing[i]
divisor=[]
for i in range(1,(max_t>>1)+1):
    if max_t%i==0:
        divisor.append(i)
divisor.append(max_t)
adj=0
for t in timing:
    for d in divisor:
        if d>=t:
            adj+=d-t
            break
print(adj)