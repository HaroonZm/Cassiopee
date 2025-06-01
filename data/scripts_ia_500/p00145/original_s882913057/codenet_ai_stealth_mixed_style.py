INF = 0x7fffffff

def main():
    n = int(input())
    a = []
    for _ in range(n):
        x, y = map(int, input().split())
        a.append((x, y))

    c = [[INF]*n for _ in range(n)]
    for i in range(n):
        c[i][i] = 0

    def compute_cost(i, j):
        if i == j:
            return 0
        res = INF
        for k in range(i, j):
            left = compute_cost(i, k)
            right = compute_cost(k+1, j)
            cost = left + a[i][0]*a[k][1]*a[k+1][0]*a[j][1] + right
            if cost < res:
                res = cost
        return res

    # But to mix styles, use bottom-up DP to fill matrix partially
    for length in range(1, n):
        for start in range(n - length):
            end = start + length
            costs = []
            for mid in range(start, end):
                cost = c[start][mid] + a[start][0]*a[mid][1]*a[mid+1][0]*a[end][1] + c[mid+1][end]
                costs.append(cost)
            c[start][end] = min(costs)

    print(c[0][n-1])

if __name__ == "__main__":
    main()