n = int(input())

a = n // 10
b = n % 10

if a == 9 or b == 9:
    print('Yes')
else:
    print('No')