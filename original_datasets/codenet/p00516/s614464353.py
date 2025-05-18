n,m=[int(s)for s in input().split(" ")]
intr=[int(input())for i in range(n)]
crit=[int(input())for i in range(m)]
vote=[0 for i in range(n)]
for c in crit:
    for i in range(n):
        if intr[i]<=c:
            vote[i]+=1
            break
print(vote.index(max(vote))+1)