N, M = map(int, input().split())
a = 1900 * M
b = 100 * (N - M)
c = a + b
d = 2 ** M
e = c * d
print(e)