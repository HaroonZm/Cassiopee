def insertsort(A, N):
    print " ".join(A)
    A = map(int,A)
    for i in range(1,N):
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = v
        out_A = map(str,A)
        print " ".join(out_A)
    return A

n =  int(raw_input())
array = raw_input().split()
insertsort(array, n)