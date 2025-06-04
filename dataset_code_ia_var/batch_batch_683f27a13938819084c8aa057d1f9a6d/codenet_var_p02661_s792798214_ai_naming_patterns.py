from statistics import median

count = int(input())
values_a = [None] * count
values_b = [None] * count
for index in range(count):
    value_a, value_b = map(int, input().split())
    values_a[index], values_b[index] = value_a, value_b

if count % 2 == 1:
    result = abs(median(values_b) - median(values_a)) + 1
else:
    result = int(abs(median(values_b) - median(values_a)) * 2) + 1

print(result)