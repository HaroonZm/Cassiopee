n,m=[int(s)for s in input().split(" ")]
intr=[int(input())for i in range(n)]
crit=[int(input())for i in range(m)]
vote=[0]*n
max_vote=-1
max_index=-1
for c in crit:
    for i in range(n):
        if intr[i]<=c:
            vote[i]+=1
            break
for i in range(n):
    if vote[i]>max_vote:
        max_vote=vote[i]
        max_index=i
print(max_index+1)