h,w=map(int,input().split())
s=[]
for _ in range(h):
    s.append(list(input()))

dx=[-1,-1,-1,0,0,1,1,1]
dy=[1,0,-1,1,-1,1,0,-1]

for i in range(h):
    for j in range(w):
        if s[i][j]=="#":
            continue

        count=0
        for k in range(8):
            di=i+dx[k]
            dj=j+dy[k]

            if (di<0)|(di>h-1):
                continue
            if (dj<0)|(dj>w-1):
                continue

            if s[di][dj]=="#":
                count+=1

        s[i][j]=str(count)

for _ in range(h):
    print("".join(s[_]))