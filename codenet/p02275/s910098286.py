def countingsort(A, k):
    res = [None for _ in A]
    C = [0 for i in range(k + 1)]

    for x in A:
        C[x] += 1

    for i in range(k):
        C[i + 1] = C[i + 1] + C[i]

    for x in reversed(A):
        res[C[x] - 1] = x
        C[x] -= 1

    return res

input()
A = list(map(int, input().split()))
ret = countingsort(A, 10000)
print(" ".join(map(str, ret)))