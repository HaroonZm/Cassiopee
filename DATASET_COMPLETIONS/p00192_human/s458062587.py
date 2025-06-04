from collections import deque

class Car:
  def __init__(self, rem, ind):
    self.ind = ind
    self.rem = rem
 
class Part:
  def __init__(self, i):
    self.ind = i
    self.top = None
    self.und = None
    self.sta = 0
    self.rem = -1
  
  def prog(self, time):
    if self.top != None:
      self.top.rem -= time
    if self.und != None:
      self.und.rem -= time
    if self.sta != 0:
      self.rem -= time

  def out(self):
    if self.sta == 2:
      if self.und.rem <= 0 and self.top.rem <= 0:
        outs = [self.und.ind, self.top.ind]
        self.und = None
        self.top = None
        self.sta = 0
        self.rem = -1
        return outs
      if self.und.rem <= 0:
        outs =  [self.und.ind]
        self.und = None
        self.sta = 1
        self.rem = self.top.rem
        return outs
    
    if self.sta == 1:
      if self.top.rem <= 0:
        outs = [self.top.ind]
        self.top = None
        self.sta = 0
        self.rem = -1
        return outs
    return []

  def into(self, rem, ind):
    if self.sta == 0:
      self.top = Car(rem, ind)
      self.sta = 1
      self.rem = rem
    elif self.sta == 1:
      self.und = Car(rem, ind)
      self.sta = 2
      self.rem = rem

class Parking:
  def __init__(self, length):
    self.length = length
    self.max_space = length * 2
    self.space = length * 2
    self.body = [Part(i) for i in range(length)]

  def prog(self, time):
    for part in self.body:
      part.prog(time)

  def out(self):
    outs = []
    for part in self.body:
      if part.sta >= 1 and part.rem <= 0:
        outs.append(part.out())
    ret = []
    for out in outs:
      ret += out
    self.space += len(ret)
    return ret

  def into(self, rem, ind):
    self.space -= 1
    for part in self.body:
      if part.sta == 0:
        part.into(rem, ind)
        return
    
    rem_lst = []
    for part in self.body:
      if part.sta == 1:
        rem_lst.append((part.rem, part.ind))
    rem_lst.sort()
    
    for r, i in rem_lst:
      if r >= rem:
        self.body[i].into(rem, ind)
        return
    
    max_r = r
    for r, i in rem_lst:
      if r == max_r:
        self.body[i].into(rem, ind)
        return

while True:
  m, n = map(int, input().split())
  if m == 0:
    break
  parking = Parking(m)
  que = deque()
  ans = []
  for t in range(n * 120 - 1):
    parking.prog(1)
    ans += parking.out()
    if t <= (n - 1) * 10 and t % 10 == 0:
      r = int(input())
      que.append((r, t // 10 + 1))

    for i in range(min(parking.space, len(que))):
      rem, ind = que.popleft()
      parking.into(rem, ind)
  print(*ans)