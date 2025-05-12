import math
n=int(input())
a=list(map(int, input().split()))
mn=min(a)
mx=max(a)
print(math.ceil((mn+mx)/2)-mn)