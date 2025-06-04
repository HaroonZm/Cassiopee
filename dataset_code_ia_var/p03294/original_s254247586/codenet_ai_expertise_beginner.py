n = int(input())
a = input().split()
total = 0
for i in range(len(a)):
    total = total + int(a[i])
result = total - n
print(result)