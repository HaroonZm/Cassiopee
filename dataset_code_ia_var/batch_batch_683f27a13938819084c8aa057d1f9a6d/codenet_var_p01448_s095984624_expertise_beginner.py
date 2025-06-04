n = int(input())
table = [0] * 100003
table[0] = 1

for i in range(n):
    line = input()
    parts = line.split()
    a = int(parts[0])
    b = int(parts[1])
    table[a] += 1
    table[b + 1] -= 1

for i in range(1, len(table)):
    table[i] = table[i] + table[i - 1]

ans = 0
for i in range(len(table)):
    if table[i] >= i:
        ans = i

print(ans - 1)