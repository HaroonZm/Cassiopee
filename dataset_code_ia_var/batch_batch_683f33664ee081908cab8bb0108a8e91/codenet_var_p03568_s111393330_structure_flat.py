n = int(input())
a = list(map(int, input().split()))
even_count = 0
i = 0
while i < n:
    if a[i] % 2 == 0:
        even_count += 1
    i += 1
result = 1
j = 0
while j < n:
    result *= 3
    j += 1
power = 1
k = 0
while k < even_count:
    power *= 2
    k += 1
print(result - power)