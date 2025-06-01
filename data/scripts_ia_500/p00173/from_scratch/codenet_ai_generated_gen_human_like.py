classes = []
for _ in range(9):
    line = input().split()
    name = line[0]
    a = int(line[1])
    b = int(line[2])
    total = a + b
    revenue = a * 200 + b * 300
    classes.append((name, total, revenue))

for c in classes:
    print(c[0], c[1], c[2])