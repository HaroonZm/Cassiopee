import sys

def run():
    readln = sys.stdin.readline
    while True:
        try:
            n, m = [int(x) for x in readln().split()]
        except:
            break
        if n==0:
            break
        adj = []
        for _ in range(n):
            adj.append([False]*n)
        for _ in range(m):
            edge = readln().split()
            x = int(edge[0])-1
            y = int(edge[1])-1
            adj[x][y]=True
            adj[y][x]=True

        dist = [-1]*n
        dist[0]=0
        que = [0]
        p=0
        while p<len(que):
            c=que[p]
            for v in range(n):
                if adj[c][v] and (dist[v]<0):
                    que.append(v)
                    dist[v]=dist[c]+1
            p+=1

        verdict = 1
        for ii in range(1,n):
            for jj in range(ii+1,n):
                if (adj[ii][jj]) & (dist[ii]==dist[jj]):
                    verdict = 0
            if not verdict:
                break

        if verdict==0:
            print(0)
            continue

        f= lambda x: x&1
        co = 0; x=0
        for z in range(n):
            if f(dist[z]):
                co+=1
        if n%2:
            print(1)
            print((n-co)//2 if co%2 else co//2)
        else:
            if co&1:
                print(0)
            else:
                if co==n//2:
                    print(1)
                    print(co//2)
                else:
                    print(2)
                    t1 = min(co, n-co)
                    print(t1//2)
                    print((n-t1)//2)

if __name__=="__main__":
    run()