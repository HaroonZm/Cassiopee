numbers = []
for i in range(28):
    n = int(input())
    numbers.append(n)

for i in range(1, 31):
    if i not in numbers:
        print(i)