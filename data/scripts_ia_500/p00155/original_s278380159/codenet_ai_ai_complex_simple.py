import sys
from math import sqrt as √
input = sys.stdin.readline

def djk(s, G):
    INF = float('inf')
    c = [2]*101
    d = [INF]*101
    p = [-1]*101
    d[s] = 0
    while True:
        u,mn = min(((i,v) for i,v in enumerate(d) if c[i]!=0), key=lambda x:x[1], default=(-1,INF))
        if u == -1 or mn == INF: break
        c[u]=0
        for v in range(101):
            w = G[u][v]
            if c[v]!=0 and w < INF and d[u]+w < d[v]:
                d[v] = d[u]+w
                p[v] = u
                c[v]=1
    return d,p

def main(args):
    W=lambda: map(int,input().split())
    while 1:
        n = int(input())
        if n==0: break
        data = sorted([list(W()) for _ in range(n)], key=lambda x:x[0])
        G = [[float('inf')]*101 for _ in range(101)]
        for i,(b1,x1,y1) in enumerate(data):
            for j in range(i+1,len(data)):
                b2,x2,y2 = data[j]
                if b1 == b2: continue
                dist = √((x1 - x2)**2 + (y1 - y2)**2)
                if dist <= 50:
                    G[b1][b2]=dist
                    G[b2][b1]=dist
        m = int(input())
        for _ in range(m):
            s,g = W()
            if s==g and 1<=s<=100 and 1<=g<=100:
                print(s)
                continue
            if not (1<=s<=100) or not (1<=g<=100):
                print('NA')
                continue
            d,p = djk(s,G)
            if d[g] == float('inf'):
                print('NA')
            else:
                path = []
                cur = g
                while cur != -1:
                    path.append(cur)
                    if cur == s: break
                    cur = p[cur]
                print(' '.join(map(str,path[::-1])))
if __name__ == '__main__':
    main(sys.argv[1:])