n, m = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
memo = dict()
stack = []
stack.append((0, 0, 0, 0, 0, 0))
res = None
calc_stack = []
calc_results = {}
while stack:
    a, b, skip, turn, a_stack, b_stack = stack.pop()
    key = (a, b, skip, turn, a_stack, b_stack)
    if key in memo:
        continue
    done = False
    while not done:
        if skip == 3:
            memo[key] = 0
            done = True
            continue
        if turn % 2 == 0:
            if (a, b, skip + 1, 1, 0, 0) in memo:
                v1 = memo[(a, b, skip + 1, 1, 0, 0)] + a_stack - b_stack
            else:
                stack.append((a, b, skip, turn, a_stack, b_stack))
                stack.append((a, b, skip + 1, 1, 0, 0))
                break
            if a == len(A):
                memo[key] = v1
                done = True
                continue
            if A[a] == -1:
                next_b_stack = 0
            else:
                next_b_stack = b_stack
            next_a_stack = a_stack
            if A[a] == -1:
                next_a_stack = 0
            else:
                next_a_stack = a_stack + A[a]
            if (a + 1, b, 0, 1, next_a_stack, next_b_stack) in memo:
                v2 = memo[(a + 1, b, 0, 1, next_a_stack, next_b_stack)]
            else:
                stack.append((a, b, skip, turn, a_stack, b_stack))
                stack.append((a + 1, b, 0, 1, next_a_stack, next_b_stack))
                break
            memo[key] = max(v1, v2)
            done = True
        else:
            if (a, b, skip + 1, 0, 0, 0) in memo:
                v1 = memo[(a, b, skip + 1, 0, 0, 0)] - b_stack + a_stack
            else:
                stack.append((a, b, skip, turn, a_stack, b_stack))
                stack.append((a, b, skip + 1, 0, 0, 0))
                break
            if b == len(B):
                memo[key] = v1
                done = True
                continue
            if B[b] == -1:
                next_a_stack = 0
            else:
                next_a_stack = a_stack
            next_b_stack = b_stack
            if B[b] == -1:
                next_b_stack = 0
            else:
                next_b_stack = b_stack + B[b]
            if (a, b + 1, 0, 0, next_a_stack, next_b_stack) in memo:
                v2 = memo[(a, b + 1, 0, 0, next_a_stack, next_b_stack)]
            else:
                stack.append((a, b, skip, turn, a_stack, b_stack))
                stack.append((a, b + 1, 0, 0, next_a_stack, next_b_stack))
                break
            memo[key] = min(v1, v2)
            done = True
res = memo[(0,0,0,0,0,0)]
print(res)