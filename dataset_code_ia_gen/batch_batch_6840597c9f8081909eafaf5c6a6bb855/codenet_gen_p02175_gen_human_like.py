X, A, B = map(int, input().split())
N = int(input())
length = X
for _ in range(N):
    action = input()
    if action == "nobiro":
        length += A
    elif action == "tidime":
        length += B
    elif action == "karero":
        length = 0
    if length < 0:
        length = 0
print(length)