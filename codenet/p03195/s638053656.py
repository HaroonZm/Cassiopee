n = int(input())
a = [int(input()) for i in range(n)]
print('second' if all(a[i] % 2 == 0 for i in range(n)) else 'first')