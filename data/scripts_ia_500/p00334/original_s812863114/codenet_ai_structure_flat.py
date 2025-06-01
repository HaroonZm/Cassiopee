N=int(input())
S=set()
for _ in [0]*N:
    ligne=input().split()
    nums=[]
    for x in ligne:
        nums.append(int(x))
    nums.sort()
    S.add(str(nums))
print(N-len(S))