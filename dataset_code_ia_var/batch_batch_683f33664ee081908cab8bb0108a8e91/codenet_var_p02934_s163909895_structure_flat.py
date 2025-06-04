n = int(input())
line = list(map(int, input().split()))

total = 0
i = 0
while i < n:
    total += 1 / line[i]
    i += 1

result = 1 / total
print(result)