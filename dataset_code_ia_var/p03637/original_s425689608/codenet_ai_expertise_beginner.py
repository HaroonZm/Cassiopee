n = int(input())
numbers = input().split()
count = 0

for i in range(n):
    num = int(numbers[i])
    if num % 4 == 0:
        count = count + 1
    elif num % 2 == 0:
        count = count + 0.5

if count >= n // 2:
    print("Yes")
else:
    print("No")