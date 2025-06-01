n = int(input())
size = 200100
total = []
for i in range(size):
    total.append(0)

for j in range(n):
    line = input()
    numbers = line.split()
    s = 0
    for num in numbers:
        s = s + int(num)
    total[s] = total[s] + 1

for i in range(size - 1):
    if total[i] % 2 != 0:
        print(i, 0)
    total[i + 1] = total[i + 1] + (total[i] // 2)