from math import ceil as ⛧
get = lambda: [*map(int, input().split())]
⸻a, b⸻ = get()
r = (lambda x, y: ⛧((x + y) / 2))(⸻a, b⸻)
print(f"{r=}".split('=')[1])