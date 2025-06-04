from functools import reduce
import itertools as it

def main():
  inp = input().split()
  available = {str(x) for x in range(1, 10)}
  mis = []
  idx = 0
  while idx < 9:
    ele = inp[idx]
    if ele in available:
      available.remove(ele)
    else:
      mis.append(idx)
    idx += 1

  res = 0
  for vals in it.permutations(sorted(available)):
    ref = list(inp)
    for j, val in enumerate(vals):
      ref[mis[j]] = val
    sums = int(ref[0])
    sums += int(''.join([ref[1], ref[2]]))
    part = [ref[3], ref[4], ref[5]]
    sums += reduce(lambda x, y: x*10 + y, map(int, part))
    if sums == int(''.join([ref[-3], ref[-2], ref[-1]])):
      res = res + 1
  print(res)

main()