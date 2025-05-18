H,W = map(int,input().split())
if (H*W)%3==0:
    dif = 0
else:
    dif = min(H,W)
    for i in range(1,W//2+1):
        s1 = H*i
        s2 = (W-i)*(H//2)
        s3 = (W-i)*(H-H//2)
        d = max(s1,s2,s3)-min(s1,s2,s3)
        dif = min(dif,d)
    for j in range(1,H//2+1):
        s1 = W*j
        s2 = (H-j)*(W//2)
        s3 = (H-j)*(W-W//2)
        d = max(s1,s2,s3)-min(s1,s2,s3)
        dif = min(dif,d)
print(dif)