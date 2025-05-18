def bubble_sort(A, N):
    flag = True
    c = 0
    i = 0
    while flag:
        flag = False
        for j in range(N-1, i, -1):
            if A[j] < A[j-1]:
                A[j],  A[j-1] = A[j-1], A[j]
                c += 1
                flag = True
        i += 1

    return c

while True:

    N = int(raw_input())

    if N == 0:
        break

    A = [int(raw_input()) for _ in xrange(N)]

    print bubble_sort(A, N)