from collections import defaultdict
def soinnsuubunnkai(n):
  dic = defaultdict(int)
  i = 2
  while i * i <= n:
    while n % i == 0:
      dic[i] += 1
      n //= i
    i += 1
  if n != 1:
    dic[n] += 1
  return list(dic.values())
  
def saiki(values, score, ind, end):
  if ind == end:
    return score
  return saiki(values, score * values[ind], ind + 1, end) * 2+ \
         saiki(values, score, ind + 1, end)

while True:
  n = int(input())
  if n == 0:
    break
  values = soinnsuubunnkai(n)
  print((saiki(values, 1, 0, len(values)) + 1) // 2)