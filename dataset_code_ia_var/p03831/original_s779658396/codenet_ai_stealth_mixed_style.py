def calculate_moves():
  from functools import reduce
  x = input()
  y = input()
  args = list(map(int, x.split()))
  steps = y.split()
  m = 0
  [N, A, B] = args[0], args[1], args[2]
  def compute(i, m):
      gap = int(steps[i+1]) - int(steps[i])
      return m + (B if (gap)*A >= B else A*gap)
  idx = 0
  while idx < N-1:
      m = compute(idx, m)
      idx += 1
  print(m)
calculate_moves()