n = int(input())
numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
numbers.sort()
result = numbers[len(numbers)-1] - numbers[0]
print(result)