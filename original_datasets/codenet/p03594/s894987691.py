H,W,d = map(int,input().strip().split())
colors = ('R','Y','G','B')
for i in range(H):
    line = []
    for j in range(W):
        x = (i+j)%(2*d) >= d
        y = (i-j)%(2*d) >= d
        line.append(colors[2*x+y])
    print(''.join(line))