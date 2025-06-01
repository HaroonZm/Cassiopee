import sys
input = sys.stdin.readline

N,K,L = map(int, input().split())
a = list(map(int, input().split()))

class BIT:
    def __init__(self,n):
        self.n = n+1
        self.bit = [0]*(self.n)
    def add(self,i,x):
        while i<self.n:
            self.bit[i]+=x
            i+=i&-i
    def sum(self,i):
        s=0
        while i>0:
            s+=self.bit[i]
            i-=i&-i
        return s
    def range_sum(self,l,r):
        return self.sum(r) - self.sum(l-1)

def check(x):
    bit = BIT(N)
    cnt = 0
    left = 0
    for right in range(N):
        if a[right]<=x:
            bit.add(right+1,1)
        while right - left +1 >0 and bit.range_sum(left+1,right+1) < K:
            if a[left] <= x:
                bit.add(left+1,-1)
            left+=1
        length = right - left +1
        if length >= K:
            cnt += length - K +1
        if cnt >= L:
            return True
    return False

low, high = 1, N
while low<high:
    mid=(low+high)//2
    if check(mid):
        high=mid
    else:
        low=mid+1
print(low)