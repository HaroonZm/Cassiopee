L,N = [int(i) for i in input().split()]
snake = input()

d = 0
for i in range(L-1):
    if snake[i] == "o" and snake[i+1] == "o":
        d += 1

ans = L    
for i in range(N):
    ans += d * 3
    d *= 2

print(ans)