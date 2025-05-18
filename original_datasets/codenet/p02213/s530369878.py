H,W = map(int,input().split())
S = [list(input()) for i in range(H)]

A = [[False]*W for i in range(H)]

Q = [(0,0,(5,4,1,3,6,2))]

while Q:
    q = Q.pop()
    h,w,s = q[0],q[1],q[2]
    if min(h,w)<0 or h>=H or w>=W:continue
    if S[h][w]=="#":continue
    if A[h][w]:continue
    if int(S[h][w])!=s[4]:continue
    A[h][w] = True
    Q.append((h-1,w,(s[2],s[1],s[5],s[3],s[0],s[4])))
    Q.append((h+1,w,(s[4],s[1],s[0],s[3],s[5],s[2])))
    Q.append((h,w-1,(s[0],s[2],s[3],s[4],s[1],s[5])))
    Q.append((h,w+1,(s[0],s[4],s[1],s[2],s[3],s[5])))
print("YES" if A[H-1][W-1] else "NO")