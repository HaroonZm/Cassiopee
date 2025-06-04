odd = {0: 1}
even = {0: 1, 1: 3}
M = 10**9 + 7

n = int(input())

N = n
stack = []
memo_res = {}
while True:
    if N == 0:
        memo_res[N] = 1
        break
    if N == 1:
        memo_res[N] = 2
        break
    stack.append(N)
    N = (N - 1) // 2

while stack:
    N = stack.pop()
    n1 = (N - 1) // 2
    n2 = N // 2

    # For odd
    if n1 in odd:
        a = odd[n1]
    else:
        a = memo_res.get(n1, None)
        if a is None:
            a = 1 if n1 == 0 else 2
    # For even
    if n2 in even:
        b = even[n2]
    else:
        b = memo_res.get(n2, None)
        if b is None:
            b = 1 if n2 == 0 else (3 if n2 == 1 else 2)
    memo_res[N] = (a + b) % M
    odd[N] = memo_res[N]

# Now rebuild intermediate memo values for even dict
for k in range(n + 1):
    if k not in even:
        if k - 1 in memo_res and k in memo_res:
            even[k] = (memo_res[k] + memo_res[k - 1]) % M
        elif k == 0:
            even[k] = 1
        elif k == 1:
            even[k] = 3

result = memo_res.get(n, None)
if result is None:
    if n == 0:
        result = 1
    elif n == 1:
        result = 2
    else:
        result = (odd[(n - 1) // 2] + even.get(n // 2, 1)) % M
print(result)