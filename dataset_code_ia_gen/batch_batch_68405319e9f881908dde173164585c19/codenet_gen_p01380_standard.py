N=int(input())
probs=[tuple(map(int,input().split())) for _ in range(N)]
probs.sort(key=lambda x:x[1])
time=0
count=0
for a,b in probs:
    time+=a
    if time<=b:
        count+=1
print(count)