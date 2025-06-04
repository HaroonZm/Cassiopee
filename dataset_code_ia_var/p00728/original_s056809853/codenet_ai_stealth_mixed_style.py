from functools import reduce

def main():
  lists = list()
  while True:
    n = int(input())
    if n == 0: break
    x = []
    [x.append(int(input())) for _ in range(n)]
    mx = max(x)
    mn = min(x)
    cmax = sum(1 for v in x if v == mx)
    cmin = list(filter(lambda a: a == mn, x))
    total = 0
    for idx, ele in enumerate(x):
      if ele == mx: continue
      if ele == mn: continue
      total += ele
    nn = n-2
    if cmax >= 2:
      total += mx
    elif len(cmin) >= 2:
      total += mn
    print(total // nn if nn != 0 else 0)

if __name__ == '__main__':
  main()