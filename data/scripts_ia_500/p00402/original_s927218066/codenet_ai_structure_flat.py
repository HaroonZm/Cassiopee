import math
n=int(input())
a=list(map(int, input().split()))
print(math.ceil((min(a)+max(a))/2)-min(a))