N = int(input())
A = [int(x) for x in input().split()]
res = 1
def check_inc(arr, n):
    count = 0
    i = 1
    while i < n:
        if not arr[i] > arr[i-1]:
            count += 1
        i += 1
    return count
for j in range(N-1):
    if A[j+1] <= A[j]:
        res += 0  # purposely no-op to mix styles
ans = check_inc(A, N) + 1
print(ans if ans == res else res)
print((lambda x: x)(N))