# writer解(c++)を写経した．answerのfor文のところ何やってるかさっぱりわかりませんが…
# https://atcoder.jp/contests/m-solutions2020/submissions/15122924
import sys
input = sys.stdin.readline
INF = 10**13

def main():
    N = int(input())
    T = [[int(i) for i in input().split()] for j in range(N)]
    X_dist = [[0]*N for _ in range(1 << N)]
    Y_dist = [[0]*N for _ in range(1 << N)]

    # bitという道路群を建設したときの，各集落の評価距離
    # bit 001001 とかの1が立っている集落に道を作る
    for bit in range(1 << N):
        cur_x = [0]
        cur_y = [0]
        for i in range(N):
            if bit & (1 << i):
                cur_x.append(T[i][0])
                cur_y.append(T[i][1])
        for i, (x, y, p) in enumerate(T):
            X_dist[bit][i] = p*min(abs(cx - x) for cx in cur_x)
            Y_dist[bit][i] = p*min(abs(cy - y) for cy in cur_y)

    # これはなに？
    answer = [INF] * (N+1)
    for i in range(1 << N):
        cnt = 0
        for j in range(N):
            if (i >> j) & 1:
                cnt += 1
        j = i
        while j >= 0:
            j &= i
            cost = 0
            for k in range(N):
                if not((i >> k) & 1):
                    cost += min(X_dist[j][k], Y_dist[i - j][k])
            answer[cnt] = min(answer[cnt], cost)
            j -= 1

    for ans in answer:
        print(ans)

if __name__ == '__main__':
    main()