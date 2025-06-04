d = {
    0: lambda x, y: max(x, y),
    1: lambda x, y: min(x, y)
}

while True:
    n = int(input())
    if n == 0:
        break
    ans = [0, 500]
    for _ in range(n):
        score = sum(map(int, input().split()))
        ans = [
            d[i](ans[i], score)
            for i in range(2)
        ]
    print(*ans)