n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
memo = {}
stack = [(0, 0, 0, 0, 1, 0)]
visited = {}
while stack:
    state = stack[-1]
    if state in memo:
        stack.pop()
        continue
    p, q, s, t, turn, pss = state
    if (state in visited and not visited[state]):
        stack.pop()
        if p == len(A) and q == len(B):
            memo[state] = s-t
        else:
            if turn:
                res = visited[(state, 'res')]
                if p < len(A):
                    if A[p] == -1:
                        res = max(res, memo.get((p+1, q, s, 0, 0, 0), 0))
                    else:
                        res = max(res, memo.get((p+1, q, s+A[p], t, 0, 0), 0))
                memo[state] = res
            else:
                res = visited[(state, 'res')]
                if q < len(B):
                    if B[q] == -1:
                        res = min(res, memo.get((p, q+1, 0, t, 1, 0), 0))
                    else:
                        res = min(res, memo.get((p, q+1, s, t+B[q], 1, 0), 0))
                memo[state] = res
        continue
    if p == len(A) and q == len(B):
        memo[state] = s-t
        stack.pop()
        continue
    if turn:
        if pss < 2:
            if s+t:
                stack[-1] = (p, q, s, t, turn, pss, 'ready')
                key = (p, q, 0, 0, 0, 0)
                if key not in memo:
                    stack.append(key)
                else:
                    visited[(state, 'res')] = (s-t) + memo[key]
                    visited[state] = False
            else:
                stack[-1] = (p, q, s, t, turn, pss, 'ready')
                key = (p, q, 0, 0, 0, pss+1)
                if key not in memo:
                    stack.append(key)
                else:
                    visited[(state, 'res')] = memo[key]
                    visited[state] = False
        else:
            memo[state] = 0
            stack.pop()
            continue
        if len(stack[-1]) == 7 and A and p < len(A):
            _, _, _, _, _, _, flag = stack[-1]
            if flag == 'ready':
                res = visited[(state, 'res')]
                if A[p] == -1:
                    key = (p+1, q, s, 0, 0, 0)
                    if key not in memo:
                        stack.append(key)
                        continue
                    res = max(res, memo[key])
                else:
                    key = (p+1, q, s+A[p], t, 0, 0)
                    if key not in memo:
                        stack.append(key)
                        continue
                    res = max(res, memo[key])
                visited[(state, 'res')] = res
                visited[state] = False
    else:
        if pss < 2:
            if s+t:
                stack[-1] = (p, q, s, t, turn, pss, 'ready')
                key = (p, q, 0, 0, 1, 0)
                if key not in memo:
                    stack.append(key)
                else:
                    visited[(state, 'res')] = (s-t) + memo[key]
                    visited[state] = False
            else:
                stack[-1] = (p, q, s, t, turn, pss, 'ready')
                key = (p, q, 0, 0, 1, pss+1)
                if key not in memo:
                    stack.append(key)
                else:
                    visited[(state, 'res')] = memo[key]
                    visited[state] = False
        else:
            memo[state] = 0
            stack.pop()
            continue
        if len(stack[-1]) == 7 and B and q < len(B):
            _, _, _, _, _, _, flag = stack[-1]
            if flag == 'ready':
                res = visited[(state, 'res')]
                if B[q] == -1:
                    key = (p, q+1, 0, t, 1, 0)
                    if key not in memo:
                        stack.append(key)
                        continue
                    res = min(res, memo[key])
                else:
                    key = (p, q+1, s, t+B[q], 1, 0)
                    if key not in memo:
                        stack.append(key)
                        continue
                    res = min(res, memo[key])
                visited[(state, 'res')] = res
                visited[state] = False
    if not (p == len(A) and q == len(B)) and not ((turn and p < len(A)) or (not turn and q < len(B))):
        if turn:
            visited[state] = False
        else:
            visited[state] = False
print(memo[(0,0,0,0,1,0)])