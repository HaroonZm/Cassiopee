n, k = map(int, input().split())
print(''.join((c if i != k-1 else c.lower()) for i, c in enumerate(input())))