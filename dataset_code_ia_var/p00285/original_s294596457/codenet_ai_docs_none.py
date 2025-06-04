def main():
  while True:
    m, w = map(int, input().split())
    if m == 0:
      break
    if m >= w:
      long_lst = list(map(int, input().split()))
      short_lst = list(map(int, input().split()))
      rest = 2 ** m - 1
    else:
      short_lst = list(map(int, input().split()))
      long_lst = list(map(int, input().split()))
      rest = 2 ** w - 1
    mem = [None] * (rest + 1)
    def elec(bm, bw):
      bd = abs(bm - bw)
      return bd * (bd - 30) ** 2
    def score(rest, index):
      if mem[rest] != None:
        return mem[rest]
      if rest == 0 or index < 0:
        return 0
      mask = 1
      count = 0
      ret = 0
      while mask <= rest:
        if mask & rest:
          new_rest = rest & ~mask
          ret = max(ret, score(new_rest, index - 1) + elec(short_lst[index], long_lst[count]))
        mask <<= 1
        count += 1
      mem[rest] = ret
      return ret
    print(score(rest, min(m, w) - 1))
main()