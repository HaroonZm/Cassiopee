def bubble_sort(A, N):
    flag = True
    i = 0

    while flag:
        flag = False
        for j in range(1, N-i):
            if A[j] < A[j-1]:
                A[j],  A[j-1] = A[j-1], A[j]
                flag = True
        i += 1

n = int(raw_input())
A = map(int, raw_input().split())

bubble_sort(A, n)

print " ".join([str(i) for i in A])