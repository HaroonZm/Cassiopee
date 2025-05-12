import itertools
s = input()
n = len(s) - 1

ans = 0
op = [x for x in itertools.product(["+", ""], repeat=n)]
for i in range(2 ** n):
  f = s[0]
  for j, k in zip(op[i], s[1:]):
    f += (j+k)
  ans += eval(f)
print(ans)