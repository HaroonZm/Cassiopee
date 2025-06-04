N = int(input())
a = list(map(int, input().split()))

min_value = a[0]
min_index = 1

for i in range(1, N):
    if a[i] < min_value:
        min_value = a[i]
        min_index = i + 1

print(min_index)