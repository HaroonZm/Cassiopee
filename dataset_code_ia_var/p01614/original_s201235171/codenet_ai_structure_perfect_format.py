def main():
    n = int(input())
    phrase = [tuple(map(int, input().split())) for _ in range(n)]
    m = int(input())
    ans = []
    flag = 1
    dp = [0] * 394
    for w in range(393):
        for i in range(n):
            s, l, p = phrase[i]
            if w + s <= 393:
                dp[w + s] = max(dp[w + s], dp[w] + p)
            if w + l < 393:
                dp[w + l] = max(dp[w + l], dp[w] + p)
            elif w + l >= 393 and w + s < 393:
                dp[393] = max(dp[393], dp[w] + p)
    for _ in range(m):
        w = int(input())
        if not flag:
            continue
        if dp[w]:
            ans.append(dp[w])
        else:
            flag = 0
    if flag:
        for a in ans:
            print(a)
    else:
        print(-1)

if __name__ == "__main__":
    main()