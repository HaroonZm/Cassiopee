def insertionSort(A):
    print " ".join(map(str, A))
    for i in range(1, len(A)):
        temp = A[i]
        j = i-1
        while j >= 0 and A[j] > temp:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = temp
        print " ".join(map(str, A))

N = int(raw_input())
A = map(int, raw_input().split())

insertionSort(A)