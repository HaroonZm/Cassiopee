def selection_sort(A, N):
    count = 0
    for i in range(N - 1):
        min_index = i
        for j in range(i, N):
            if A[j] < A[min_index]:
                min_index = j
        temp = A[i]
        A[i] = A[min_index]
        A[min_index] = temp
        if i != min_index:
            count = count + 1
    for x in A:
        print(x, end=" ")
    print()
    print(count)

N = int(input())
A = list(map(int, input().split()))
selection_sort(A, N)