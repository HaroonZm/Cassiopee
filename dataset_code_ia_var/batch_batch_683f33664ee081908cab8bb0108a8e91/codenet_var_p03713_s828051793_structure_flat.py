H,W = map(int,input().split())
ans = float('inf')
halfed_w = W//2
for h in range(1,H):
    a  = h*W
    b1 = (H-h)//2*W
    c1 = (H-h-(H-h)//2)*W
    b2 = (H-h)*halfed_w
    c2 = (H-h)*(W-halfed_w)
    result1 = max(a,b1,c1)-min(a,b1,c1)
    result2 = max(a,b2,c2)-min(a,b2,c2)
    if result1 < ans:
        ans = result1
    if result2 < ans:
        ans = result2
halfed_h = H//2
for w in range(1,W):
    a = w*H
    b1 = (W-w)//2*H
    c1 = (W-w-(W-w)//2)*H
    b2 = (W-w)*halfed_h
    c2 = (W-w)*(H-halfed_h)
    result1 = max(a,b1,c1)-min(a,b1,c1)
    result2 = max(a,b2,c2)-min(a,b2,c2)
    if result1 < ans:
        ans = result1
    if result2 < ans:
        ans = result2
print(ans)