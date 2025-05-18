class Dice:

  def __init__(self, top=1, front=2, left=4, right=3, back=5, bottom=6):
    self.d = {"TOP": top, "FRONT": front, "LEFT": left, "RIGHT": right, "BACK": back, "BOTTOM": bottom}

  def roll_x(self):
    self._roll("TOP", "FRONT", "BOTTOM", "BACK")

  def roll_y(self):
    self._roll("FRONT", "LEFT", "BACK", "RIGHT")

  def roll_z(self):
    self._roll("TOP", "LEFT", "BOTTOM", "RIGHT")

  def _roll(self, a, b, c, d):
    self.d[a], self.d[b], self.d[c], self.d[d] = self.d[b], self.d[c], self.d[d], self.d[a]

  def all_rolls(self):
    import copy
    ret = []
    for i in range(6):
      if i % 2:
        self.roll_x()
      else:
        self.roll_y()
      for _ in range(4):
        self.roll_z()
        ret.append(copy.deepcopy(self))
    return ret

import copy
from collections import defaultdict
while True:
  n = int(input())
  if n==0:
    break

  board = [[0 for i in range(100)] for j in range(100)]
  height = [[0 for i in range(100)] for j in range(100)]

  for i in range(n):
    t, f = list(map(int, input().split()))
    dice = Dice()
    for di in dice.all_rolls():
      if di.d["TOP"]==t and di.d["FRONT"]==f:
        break

    x, y = 50, 50
    while True:
      dxy = []
      for s in ["FRONT", "LEFT", "BACK", "RIGHT"]:
        tt = di.d[s]
        if tt>=4:
          dxy.append((tt, s))
      dxy.sort(reverse=True)

      move = False
      for _, s in dxy:
        newdice = copy.deepcopy(di)
        if s=="FRONT":
          dx = 0
          dy = 1
          newdice.roll_x()
          newdice.roll_x()
          newdice.roll_x()
        elif s=="LEFT":
          dx = -1
          dy = 0
          newdice.roll_z()
          newdice.roll_z()
          newdice.roll_z()
        elif s=="BACK":
          dx = 0
          dy = -1
          newdice.roll_x()
        elif s=="RIGHT":
          dx = 1
          dy = 0
          newdice.roll_z()

        if height[x][y]>height[x+dx][y+dy]:
          x = x+dx
          y = y+dy
          di = newdice
          move = True
          break

      if not move:
        board[x][y] = di.d["TOP"]
        height[x][y] += 1
        break

  ans = defaultdict(int)
  for e in board:
    for ee in e:
      ans[ee] += 1
  print(*[ans[i] for i in range(1, 7)])