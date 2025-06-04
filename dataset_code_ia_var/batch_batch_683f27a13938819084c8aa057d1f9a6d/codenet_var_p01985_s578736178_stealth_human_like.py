import sys
input = sys.stdin.readline

def main():
    # ok, so, I'll just keep looping forever (until N is 0!)
    while True:
        N, M = map(int, input().split())
        if N == 0:
            break  # that's enough
        # adjacency matrix - maybe not the best idea but w/e
        path = []
        for _ in range(N):
            row = [False]*N
            path.append(row)
        # read M edges
        for _ in range(M):
            u, v = input().split()
            u = int(u)-1
            v = int(v)-1
            path[u][v] = True
            path[v][u] = True
        # distances from node 0... (BFS, a bit naive but works)
        dist = [-1]*N
        dist[0] = 0
        queue = [0]  # use list, inefficient I know
        while queue:
            current = queue.pop(0)
            for i in range(N):
                if path[current][i]:
                    if dist[i]==-1:
                        dist[i] = dist[current]+1
                        queue.append(i)
        # check for odd-length cycles (?) - bipartite test?
        is_bipartite = True
        for i in range(1, N):
            for j in range(i+1, N):
                # not my favourite variable names tbh
                if path[i][j] and dist[i]==dist[j]:
                    is_bipartite = False
                    break
            if not is_bipartite:
                break
        if not is_bipartite:
            print(0)
            continue
        cnt = 0
        for i in range(N):
            if dist[i]%2==1:
                cnt += 1
        # I'm not 100% sure about all these if/elses, but it seems to work
        if N%2==1:
            print(1)
            if cnt%2==1:
                print((N - cnt)//2)
            else:
                print(cnt//2)
        else:
            if cnt%2==1:
                print(0)
            else:
                if cnt*2 == N:
                    print(1)
                    print(cnt//2)
                else:
                    print(2)
                    x = min(cnt, N-cnt)
                    print(x//2)
                    print((N-x)//2)

if __name__=="__main__":
    main()