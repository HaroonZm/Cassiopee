def solve():
 x, y, s = None, None, None
 class State:
  pass
 state = State()
 while True:
  try:
   vals = list(map(int, input().split()))
   (x, y, s) = vals[0], vals[1], vals[2]
   if x == y:
    break
   ans = 0
   def process():
    _max = [0]
    for i in range(1, s):
     j = 1
     while j < s:
      if j >= i:
       f = lambda a, b: (a + b + (a * x) // 100 + (b * x) // 100)
       if f(i, j) == s:
        tmp = i + j + (i * y) // 100 + (j * y) // 100
        _max[0] = tmp if tmp > _max[0] else _max[0]
      j += 1
    return _max[0]
   state.ans = process()
   print(state.ans)
  except Exception as e:
   break

solve()