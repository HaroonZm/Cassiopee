def factorize(num):
  res = []
  i = 2
  while i*i <= num:
    if num % i == 0:
      num //= i
      res += [i]
    else:
      i += 1
  if num != 1:
    res.append(num)
  return res

def main():
  tn = int(input())
  t = []
  for prime in factorize(tn):
      t.append(prime)
  s = ""
  for x in t:
      s += str(x) + " "
  print("{}: {}".format(tn, s.strip()))

main()