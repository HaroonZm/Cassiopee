total = 0
for _ in range(5):
    total += int(input())
total += sum(map(int, [input() for _ in range(5)]))
print(total)