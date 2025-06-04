numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
numbers.sort()
result = 10 * numbers[2] + numbers[1] + numbers[0]
print(result)