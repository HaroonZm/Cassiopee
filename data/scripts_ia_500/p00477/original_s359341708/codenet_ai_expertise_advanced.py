t = sum(int(input()) for _ in range(4))
g = max(0, (t + 59) // 60 - 1)
print(g)
print(t % 60)