def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            tmp = A[j]
            A[j] = A[i]
            A[i] = tmp
        else:
            continue
    A[r] = A[i+1]
    A[i+1] = x
    return i+1

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    x = partition(a, 0, n-1) 
    A = [str(a[i]) for i in range(n)]
    A[x] = '[' + A[x] + ']'
    for i in range(n):
        if i == n-1:
            print(A[i])
        else:
            print(A[i], end=' ')
main()