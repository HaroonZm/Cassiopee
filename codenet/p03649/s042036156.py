def check(N, A, n):
    for i in range(min(n, N)+1):
        x = n - i
        cnt = 0
        for a in A:
            if a + x >= N:
                cnt += -(-(a + x - N + 1)//(N+1))
        if cnt <= x:
            return True
    return False

def main():
    N = int(input())
    A = list(map(int, input().split()))
    lo = 0
    hi = int(1e18)
    while lo < hi:
        mid = (lo + hi) // 2
        if check(N, A, mid):
            hi = mid
        else:
            lo = mid + 1
    print(lo)

if __name__ == "__main__":
    main()