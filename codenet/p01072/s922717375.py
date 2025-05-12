w, h, t = map(int, input().split())
p = int(input())
hiryo = []
for i in range(p):
    x, y, t = list(map(int, input().split()))
    hiryo.append([x, y, t])
hatake = [[0 for i in range(w)] for j in range(h)]
hatake_boolean = []
for i in range(h):
    row = list(map(int, input().split()))
    row_boolean = []
    for j in row:
        if j: row_boolean.append(True)
        else: row_boolean.append(False)
    hatake_boolean.append(row_boolean)

for i in range(p):
    x, y, t = hiryo[i]
    if hatake_boolean[y][x]:
        hatake[y][x] += 1
ans = 0
for row in hatake:
    ans += sum(row)
print(ans)