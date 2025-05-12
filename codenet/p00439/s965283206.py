def fun(n, k):
    A = [int(input()) for _ in range(n)]
    k_sum = 0
    maximam = 0
    for num, a in enumerate(A):
        if 0 <= num <= k-1:
            k_sum += a
        else:
            maximam = max(maximam, k_sum + a - A[num-k])
            k_sum = k_sum + a - A[num-k]
    print(maximam)

for _ in range(5):
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break
    else:
        fun(n, k)