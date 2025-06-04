n = int(input())
intervals = []
highest = 0

for i in range(n):
    x, y = input().split()
    x = int(x)
    y = int(y)
    end = y + 1
    intervals.append([x, end])
    if end > highest:
        highest = end

table = [0] * (highest + 2)

for interval in intervals:
    table[interval[0]] += 1
    table[interval[1]] -= 1

for i in range(1, len(table)):
    table[i] += table[i - 1]

answer = 0
for i in range(len(table)):
    if i <= table[i] + 1 and i <= n + 1:
        if i > answer:
            answer = i

print(answer - 1)