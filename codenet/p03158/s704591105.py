from bisect import bisect_left

N, Q = map(int, input().split())
A = [int(i) for i in input().split()]
X = [int(input()) for _ in range(Q)]

i = (N & 1) ^ 1
j = N // 2

st = sum(A[j:])

ret_k = []
ret_v = []

while i < j :
    ret_k.append((A[i] + A[j]) // 2)
    ret_v.append(st)
    st = st - A[j] + A[i]
    i += 2
    j += 1
ret_k.append(1e+12)
ret_v.append(st)

for x in X :
    print(ret_v[bisect_left(ret_k, x)])