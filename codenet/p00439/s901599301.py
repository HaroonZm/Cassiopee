def solve():
    while 1:
        n, k = [int(_) for _ in input().split()]
        if n == 0: return

        A = [int(input()) for _ in range(n)]
        s = [0] * (len(A) + 1)
        for i in range(n):
            s[i + 1] = s[i] + A[i]

        ans = -1
        for l in range(n):
            r = l + k
            if r > n: break
            ans = max(ans, s[r] - s[l])
        print(ans)

if __name__ == '__main__':
    solve()