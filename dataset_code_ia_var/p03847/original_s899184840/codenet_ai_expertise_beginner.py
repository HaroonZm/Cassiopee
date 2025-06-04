odd = {0: 1}
even = {0: 1, 1: 3}
M = 10**9 + 7

def memo(N):
    if N == 0:
        return 1
    if N == 1:
        return 2
    return (memoodd((N - 1) // 2) + memoeven(N // 2)) % M

def memoodd(N):
    if N in odd:
        return odd[N]
    value = memo(N)
    odd[N] = value
    return value

def memoeven(N):
    if N in even:
        return even[N]
    value = (memo(N) + memo(N - 1)) % M
    even[N] = value
    return value

n = int(input())
print(memo(n))