n, x, m = map(int, input().split())
queries = [tuple(map(int, input().split())) for _ in range(m)]

best = None
max_sum = -1

def check(arr):
    for l, r, s in queries:
        if sum(arr[l-1:r]) != s:
            return False
    return True

def dfs(i, arr):
    global best, max_sum
    if i == n:
        if check(arr):
            total = sum(arr)
            if total > max_sum:
                max_sum = total
                best = arr[:]
        return
    for val in range(x+1):
        arr.append(val)
        dfs(i+1, arr)
        arr.pop()

dfs(0, [])

if best is None:
    print(-1)
else:
    print(*best)