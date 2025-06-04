import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    work = [[] for _ in range(N)]  # 各職人の工事記録（(工事種類-1, 回数)）
    total_e = 0
    while True:
        s, t, e = map(int, input().split())
        if s == 0 and t == 0 and e == 0:
            break
        work[s-1].append((t-1, e))
        total_e += e
    L = int(input())
    for _ in range(L):
        b = list(map(int, input().split()))
        c = [0]*N
        for i in range(N):
            total = 0
            for (tj, ej) in work[i]:
                total += b[tj]*ej
            c[i] = total
        print(*c)

if __name__ == "__main__":
    main()