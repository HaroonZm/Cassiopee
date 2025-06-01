n = int(input())
s = 0
for i in range(n):
    line = input()
    parts = line.split()
    a = int(parts[0])
    b = int(parts[1])
    power = a + b
    s = s + (2 ** power)
i = 0
ans = []
while s > 0:
    if s % 2 == 1:
        ans.append(i)
    s = s // 2
    i = i + 1
for e in ans:
    print(e, 0)