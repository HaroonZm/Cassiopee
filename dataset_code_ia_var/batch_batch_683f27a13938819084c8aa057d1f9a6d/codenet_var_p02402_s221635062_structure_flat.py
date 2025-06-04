n = int(input())
data = input().split()
for i in range(len(data)):
    data[i] = int(data[i])
min_value = data[0]
max_value = data[0]
total = 0
for x in data:
    if x < min_value:
        min_value = x
    if x > max_value:
        max_value = x
    total += x
print(min_value, max_value, total)