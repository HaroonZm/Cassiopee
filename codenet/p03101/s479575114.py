H,W=map(int,input().split())
h,w=map(int,input().split())
D=H*W
K=h*W+w*H-h*w
print(D-K)