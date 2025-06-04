n = int(input())
numbers = input().split()
for i in range(n):
    numbers[i] = int(numbers[i])

count = 0

for i in range(n):
    # vérifier si la position (i+1) est impaire
    if (i + 1) % 2 == 1:
        # vérifier si la valeur est impaire
        if numbers[i] % 2 == 1:
            count = count + 1

print(count)