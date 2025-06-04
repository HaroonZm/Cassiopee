n = int(input())
numbers = input().split()
even_count = 0
odd_count = 0
even_35_count = 0

for i in range(n):
    num = int(numbers[i])
    if num % 2 == 0:
        even_count = even_count + 1
        if num % 3 == 0 or num % 5 == 0:
            even_35_count = even_35_count + 1
    else:
        odd_count = odd_count + 1

if even_count == even_35_count:
    print("APPROVED")
else:
    print("DENIED")