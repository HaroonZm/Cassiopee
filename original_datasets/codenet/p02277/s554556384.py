def partition(A, p, r, key=lambda x: x):
    x = key(A[r])
    i = p - 1

    for j in range(p, r):
        if key(A[j]) <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

def quick_sort(A, p, r, key=lambda x: x):
    if p < r:
        q = partition(A, p, r, key=key)
        quick_sort(A, p, q - 1, key=key)
        quick_sort(A, q + 1, r, key=key)

if __name__ == '__main__':
    n = int(input())
    A = []
    for _ in range(n):
        egara, number = input().split()
        A.append((egara, int(number)))
    
    stable_sorted = sorted(A, key=lambda x: x[1])
    quick_sort(A, 0, n - 1, key=lambda x: x[1])

    if stable_sorted == A:
        print('Stable')
    else:
        print('Not stable')
    
    for egara, number in A:
        print(egara, number)