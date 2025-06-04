def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    MOD = 10 ** 9 + 7
    count = 0
    for i in range(N - 1):
        for j in range(i, N):
            if A[i] == A[j]:
                continue
            elif K == 1 and A[i] > A[j]:
                count += 1
            else:
                if A[i] > A[j]:
                    count += K + K * (K - 1) // 2
                else:
                    k = K - 1
                    count += k + k * (k - 1) // 2
    print(count % MOD)

main()