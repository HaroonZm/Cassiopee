def main():
  import sys
  input_iter = iter(sys.stdin.read().split())
  def inp():
    return next(input_iter)
  
  def elec(bm, bw):
    bd = abs(bm - bw)
    return bd * (bd - 30) ** 2

  while True:
    m = int(inp())
    w = int(inp())
    if m == 0:
      return

    if m >= w:
      long_lst = list(map(int, (inp() for _ in range(m))))
      short_lst = list(map(int, (inp() for _ in range(w))))
      rest = (1 << m) - 1
    else:
      short_lst = list(map(int, (inp() for _ in range(m))))
      long_lst = list(map(int, (inp() for _ in range(w))))
      rest = (1 << w) - 1

    mem = {}

    def score(rest, idx):
      if rest == 0 or idx < 0:
        return 0
      if rest in mem:
        return mem[rest]

      max_val = 0
      mask = 1
      count = 0
      while mask <= rest:
        if rest & mask:
          temp = score(rest & ~mask, idx - 1) + elec(short_lst[idx], long_lst[count])
          max_val = max(max_val, temp)
        mask <<= 1
        count += 1
      mem[rest] = max_val
      return max_val

    print(score(rest, min(m, w) - 1))

if __name__ == '__main__':
  main()