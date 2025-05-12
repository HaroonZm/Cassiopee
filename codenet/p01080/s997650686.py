def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 9)
    
    from collections import deque

    N = int(input())

    #隣接リストの作成
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)

    #直径を求める
    dist = [-1] * N
    dist[0] = 0
    que = deque()
    que.append(0) #スタート地点を入れる
    while len(que) != 0:
        tmp = que.popleft()
        for i in G[tmp]:
            if dist[i] == -1:
                dist[i] = dist[tmp] + 1
                que.append(i)
    
    tmp = 0
    start = -1
    for index, x in enumerate(dist):
        if tmp < x:
            start = index
            tmp = x
    
    dist = [-1] * N
    dist[start] = 0
    que = deque()
    que.append(start) #スタート地点を入れる
    while len(que) != 0:
        tmp = que.popleft()
        for i in G[tmp]:
            if dist[i] == -1:
                dist[i] = dist[tmp] + 1
                que.append(i)

    tmp = 0
    gpal = -1
    for index, x in enumerate(dist):
        if tmp < x:
            goal = index
            tmp = x

    dist1 = [-1] * N
    dist1[goal] = 0
    que = deque()
    que.append(goal) #スタート地点を入れる
    while len(que) != 0:
        tmp = que.popleft()
        for i in G[tmp]:
            if dist1[i] == -1:
                dist1[i] = dist1[tmp] + 1
                que.append(i)

    # print (dist)
    # print (dist1)
    for i in range(N):
        print (2 * (N - 1) - max(dist[i], dist1[i]))

if __name__ == '__main__':
    main()