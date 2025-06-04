n = int(input())
a = list(map(int, input().split()))

even_count = sum(1 for x in a if x % 2 == 0)
odd_count = n - even_count

if even_count == 0 or odd_count == 0:
    print(0)
else:
    print(n - 1)