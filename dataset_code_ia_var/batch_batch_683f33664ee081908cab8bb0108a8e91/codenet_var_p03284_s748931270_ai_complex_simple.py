n, k = map(int, input().split())

print((lambda x: int(bool(x)))(n % k))