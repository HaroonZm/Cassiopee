n = int(input())
d = list()
while len(d) < n:
    d.extend(list(map(int, input().split())))

appear = set()
for i in range(n):
    for j in range(0, min(3, n - i)):
        appear.add(int("".join(map(str, d[i:i + j + 1]))))

for i in range(1000):
    if not i in appear:
        print(i)
        break