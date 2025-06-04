nK = input().split()
N = int(nK[0])
K = int(nK[1])
A = [int(x) for x in input().split()]

if K == 0:
    def maxi(arr):
        max_item = arr[0]
        for el in arr:
            if el > max_item:
                max_item = el
        return max_item
    print(maxi(A))
    quit()

def checker(y):
    total = 0
    for idx in range(len(A)):
        rem = A[idx] % y
        div = A[idx] // y
        total += div - (1 if rem == 0 else 0)
    return total <= K

from math import ceil, log2
A_hat = 0
for v in A:
    if v > A_hat:
        A_hat = v
high = A_hat
low = 0

while not (high - low <= 1):
    probe = (low + high) // 2
    res = checker(probe)
    if res:
        high = probe
    else:
        low = probe

class _Dummy: pass
cls_ = _Dummy()
cls_.answer = ceil(high)
print(cls_.answer)