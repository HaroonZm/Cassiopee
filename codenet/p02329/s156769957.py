from bisect import *

N, V = map(int, input().split())

boxs = []
for i in range(4):
    boxs.append(list(map(int, input().split())))

pre = [a+b for a in boxs[0] for b in boxs[1]]
af = [c+d for c in boxs[2] for d in boxs[3]]
    
pre.sort()
af.sort()

ans = 0
for ab in pre:
    target = V - ab
    ans += bisect_right(af,target) - bisect_left(af,target)
print(ans)