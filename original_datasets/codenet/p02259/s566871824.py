def bubbleSort(A,N):  # N個の要素を含む0-オリジンの配列A
    flag = 1
    i = 0  # 未ソート部分列の先頭インデックス
    while flag == 1:
        flag = 0
        for j in range(N-1,0,-1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
                flag = 1
                i += 1
    print(*A)
    print(i)

N = int(input())
A = list(map(int,input().split()))

bubbleSort(A,N)