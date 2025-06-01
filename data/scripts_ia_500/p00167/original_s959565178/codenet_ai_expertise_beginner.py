def bubble_sort(A, N):
    count = 0
    i = 0
    flag = True
    while flag:
        flag = False
        j = N - 1
        while j > i:
            if A[j] < A[j - 1]:
                temp = A[j]
                A[j] = A[j - 1]
                A[j - 1] = temp
                count += 1
                flag = True
            j = j - 1
        i = i + 1
    return count

while True:
    N = int(input())
    if N == 0:
        break
    A = []
    for _ in range(N):
        A.append(int(input()))
    print(bubble_sort(A, N))