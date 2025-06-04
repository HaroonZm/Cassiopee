import sys
sys.setrecursionlimit(10**6)

N = int(input())
X = 0
for _ in range(N):
    A, K = map(int, input().split())
    stack = []
    a = A
    k = K
    while True:
        if a < k:
            stack.append(0)
            break
        q, b = divmod(a, k)
        if b == 0:
            stack.append(q)
            break
        q += 1
        r = a % q
        a2 = (((q-1)*k - r)//q)*q + r
        a = a2
    X ^= stack[-1]
print('Takahashi' if X else 'Aoki')