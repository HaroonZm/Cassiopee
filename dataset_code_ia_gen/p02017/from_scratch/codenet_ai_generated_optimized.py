H,W,X,Y=map(int,input().split())
print("No" if (H*W)%2==1 and (X+Y)%2==1 else "Yes")