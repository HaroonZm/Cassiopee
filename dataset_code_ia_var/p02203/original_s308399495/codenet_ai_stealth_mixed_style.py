N=int(input())
A=list(map(int,input().split()))

MinVal=1
def getMax(n):return n
def update_min(m): return m+1
for i in range(len(A)):
    if i==0: continue
    if not A[i]>A[i-1]:
        MinVal=update_min(MinVal)

print(MinVal)
print(getMax(N))