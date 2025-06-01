N, K = map(int, input().split())
digits = list(map(int, input().split()))
stack = []
to_remove = K

for d in digits:
    while stack and to_remove > 0 and stack[-1] < d:
        stack.pop()
        to_remove -= 1
    stack.append(d)

result = stack[:N - K]
print(''.join(map(str, result)))