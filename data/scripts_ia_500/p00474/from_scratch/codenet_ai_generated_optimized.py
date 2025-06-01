import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, L = map(int, input().split())
a = [int(input()) for _ in range(N)]

left_stack = []
left_time = [0]*N
for i in range(N):
    while left_stack and a[left_stack[-1]] < a[i]:
        left_stack.pop()
    left_time[i] = 0 if not left_stack else left_time[left_stack[-1]] + (a[i] - a[left_stack[-1]])
    left_stack.append(i)

right_stack = []
right_time = [0]*N
for i in range(N-1, -1, -1):
    while right_stack and a[right_stack[-1]] < a[i]:
        right_stack.pop()
    right_time[i] = 0 if not right_stack else right_time[right_stack[-1]] + (a[i] - a[right_stack[-1]])
    right_stack.append(i)

res = 0
for i in range(N):
    # la croissance effective est minimale entre left et right côté + temps pour atteindre L
    growth = max(left_time[i], right_time[i])
    fall_time = growth + (L - a[i])
    if fall_time > res:
        res = fall_time
print(res)