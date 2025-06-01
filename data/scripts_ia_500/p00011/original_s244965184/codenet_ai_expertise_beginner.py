n = int(input())
m = int(input())
lists = []
for i in range(m):
    line = input()
    parts = line.split(',')
    numbers = [int(parts[0]), int(parts[1])]
    lists.append(numbers)
for i in range(n):
    current = i + 1
    for pair in reversed(lists):
        if current == pair[0]:
            current = pair[1]
        elif current == pair[1]:
            current = pair[0]
    print(current)