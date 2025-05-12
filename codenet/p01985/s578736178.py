import sys
input = sys.stdin.readline

def main():
    while True:
        N, M = map(int, input().split())
        if N == 0:
            break
        path = [[False] * N for i in range(N)]
        for i in range(M):
            u, v = map(int, input().split())
            u -= 1; v -= 1;
            path[u][v] = True
            path[v][u] = True

        d = [-1] * N
        d[0] = 0
        q = [0]
        while len(q) > 0:
            now = q.pop(0)
            for i in range(N):
                if path[now][i] and d[i] == -1:
                    q.append(i)
                    d[i] = d[now] + 1
        ok = True
        for i in range(1, N):
            for j in range(i+1, N):
                if path[i][j] and d[i] == d[j]:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            print(0)
        else:
            num = 0
            for i in range(N):
                if d[i]&1:
                    num += 1
            if N&1:
                print(1)
                if num&1:
                    print((N-num)//2)
                else:
                    print(num//2)
            else:
                if num&1:
                    print(0)
                else:
                    if N//2 == num:
                        print(1)
                        print(num//2)
                    else:
                        print(2)
                        tmp = min(num, N-num)
                        print(tmp//2)
                        print((N-tmp)//2)

if __name__ == "__main__":
    main()