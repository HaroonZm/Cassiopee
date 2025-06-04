n = int(input())
a = [int(input()) for _ in range(n)]
print('second' if all(x & 1 == 0 for x in a) else 'first')