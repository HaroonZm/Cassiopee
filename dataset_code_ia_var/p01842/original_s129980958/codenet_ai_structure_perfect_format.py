n, m = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

memo = dict()

def calc(A, i):
    if A[i] != -1:
        return 0
    point = 0
    for j in range(i - 1, -1, -1):
        if A[j] == -1:
            break
        point += A[j]
    return point

def dfs(a, b, skip, turn, a_stack, b_stack):
    key = (a, b, skip, turn, a_stack, b_stack)
    if key in memo:
        return memo[key]
    if skip == 3:
        return 0
    if turn % 2 == 0:
        memo[key] = dfs(a, b, skip + 1, (turn + 1) % 2, 0, 0) + a_stack - b_stack
        if len(A) == a:
            return memo[key]
        if A[a] == -1:
            b_stack = 0
        else:
            a_stack += A[a]
        memo[key] = max(memo[key], dfs(a + 1, b, 0, (turn + 1) % 2, a_stack, b_stack))
    else:
        memo[key] = dfs(a, b, skip + 1, (turn + 1) % 2, 0, 0) - b_stack + a_stack
        if len(B) == b:
            return memo[key]
        if B[b] == -1:
            a_stack = 0
        else:
            b_stack += B[b]
        memo[key] = min(memo[key], dfs(a, b + 1, 0, (turn + 1) % 2, a_stack, b_stack))
    return memo[key]

print(dfs(0, 0, 0, 0, 0, 0))