def ___(*_):return map(int,input().split())
h__,w__=___()
r=lambda H,W:-(-(H*W)//2)if H*W>=H+W else 1
print(r(h__,w__))