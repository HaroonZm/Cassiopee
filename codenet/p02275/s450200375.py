def counting_sort(n, A, k=10001):
    C = [0 for _ in range(k)]
    B = [0 for _ in range(n)]

    for i in range(n):
        C[A[i]] += 1

    for i in range(1, k):
        C[i] = C[i] + C[i-1]

    for j in range(n-1, -1, -1):
        # C[A[j]]はA[j]以下にどれくらいの要素があるかを表している
        # したがって一番大きい数字はnになるので、-1をしてインデックス
        # をずらす必要がある
        B[C[A[j]]-1] = A[j] 
        C[A[j]] -= 1

    return B

def main():
    n = int(input())
    A = list(map(int, input().split()))
    print(*counting_sort(n, A))

if __name__ == '__main__':
    main()