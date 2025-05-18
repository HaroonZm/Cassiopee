def solve(N,T,L,B):
    route = [-1] * (N + 1)
    for _ in range(L):
        x = int(input())
        route[x] = 0
    for _ in range(B):
        y = int(input())
        route[y] = 1
    
    ans = 0
    before = [0] * (N + 1)
    before[0] = 1
    beforebefore = [0] * (N + 1)
    for _ in range(T):
        now = [0] * (N + 1)
        future = [0] *(N + 1)
        for i in range(N):
            for j in range(1,7):
                X = i + j
                if X >= N + 1:#超えた時
                    X = N - (X - N)
                if route[X] == -1:
                    now[X] += before[i]/6
                elif route[X] == 0:
                    future[X] += before[i]/6
                else:
                    now[0] += before[i]/6
        ans += now[-1]
        before = [0] * (N + 1)
        for i in range(N + 1):
            before[i] = now[i] + beforebefore[i]
        beforebefore = future
    print("{:9f}".format(ans))

def main():
    while True:
        N,T,L,B = map(int,input().split())
        if N == 0:
            return
        solve(N,T,L,B)
if __name__ == '__main__':
    main()