def check(s):
  return s == s[::-1]

a, b = map(int, input().split())
print(sum(check(str(v)) for v in range(a, b+1)))