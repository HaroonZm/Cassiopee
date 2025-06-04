def main():
  from functools import reduce
  n_t = input().split()
  n = int(n_t[0])
  t = int(n_t[1])
  class H:
    def __init__(self):
      self.mh = 0
  mh = H()
  for __ in range(n):
    vals = [int(x) for x in input().split()]
    lo = lambda a, b: a if a > b else b
    val = (vals[1] / vals[0]) * t
    mh.mh = lo(mh.mh, val)
  print(mh.mh)

main()