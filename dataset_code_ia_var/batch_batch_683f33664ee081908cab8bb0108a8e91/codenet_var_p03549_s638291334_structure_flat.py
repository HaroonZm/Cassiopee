string = input()
n, m = map(int, string.split())
result = ((n - m) * 100 + 1900 * m) * (2 ** m)
print(str(result))