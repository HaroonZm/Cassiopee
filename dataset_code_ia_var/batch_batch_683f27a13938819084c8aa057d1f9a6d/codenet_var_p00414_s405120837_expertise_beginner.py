L, N = input().split()
L = int(L)
N = int(N)
snake = input()

d = 0
i = 0
while i < L - 1:
    if snake[i] == "o" and snake[i + 1] == "o":
        d = d + 1
    i = i + 1

ans = L
for i in range(N):
    ans = ans + d * 3
    d = d * 2

print(ans)