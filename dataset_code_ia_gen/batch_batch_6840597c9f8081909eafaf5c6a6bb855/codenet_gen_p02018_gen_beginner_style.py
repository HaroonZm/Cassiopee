N = int(input())
A = list(map(int, input().split()))
count_even = 0
for num in A:
    if num % 2 == 0:
        count_even += 1
print(count_even)