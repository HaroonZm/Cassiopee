n = int(input())
a = list(map(int, input().split()))

even_count = 0
odd_count = 0

for num in a:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

if even_count == 0 or odd_count == 0:
    print(0)
else:
    # Maximum actions is total balls minus 1
    print(n - 1)