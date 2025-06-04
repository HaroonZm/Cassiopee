L = int(input())

edges = []
v = 1
base = 1
while base * 2 <= L:
    edges.append([v, v + 1, 0])
    edges.append([v, v + 1, base])
    base *= 2
    v += 1

end = edges[-1][1]
rest = L - base

for i in range(19):
    if (rest >> i) & 1:
        num = 2 ** i
        edges.append([i + 1, end, L - rest])
        rest -= num

print(v, len(edges))
for edge in edges:
    print(*edge)