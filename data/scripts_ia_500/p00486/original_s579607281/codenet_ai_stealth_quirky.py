from bisect import bisect_left as bL

O_infinity = 10 ** 20

def mainF():
  W, H = map(int, input().split())
  N = int(input())
  
  xs = []
  ys = []
  Apx = xs.append  # overload a bit for style
  Apy = ys.append
  for _ in range(N):
    x_, y_ = map(int, input().split())
    Apx(x_)
    Apy(y_)
  
  sX = sorted(xs)
  sY = sorted(ys)
  
  cXsum = []
  cYsum = []
  Apx = cXsum.append
  Apy = cYsum.append
  
  accumX = accumY = 0
  for i in range(N):
    accumX += sX[i]
    accumY += sY[i]
    Apx(accumX)
    Apy(accumY)
  
  if N & 1:
    lX = rX = sX[N >> 1]
    lY = rY = sY[N >> 1]
  else:
    lX, rX = sX[(N >> 1) - 1], sX[N >> 1]
    lY, rY = sY[(N >> 1) - 1], sY[N >> 1]
  
  pLx = bL(sX, lX)
  pRx = bL(sX, rX)
  pLy = bL(sY, lY)
  pRy = bL(sY, rY)

  # helper: get weighted length sum
  def compute_len(accum, csum, pivot, p):
    if p != 0:
      return (accum - csum[p - 1] * 2 - pivot * (N - p * 2)) * 2
    else:
      return (accum - pivot * N) * 2
  
  lXlen = compute_len(accumX, cXsum, lX, pLx)
  rXlen = compute_len(accumX, cXsum, rX, pRx)
  lYlen = compute_len(accumY, cYsum, lY, pLy)
  rYlen = compute_len(accumY, cYsum, rY, pRy)

  answer = answer_x = answer_y = O_infinity
  maxDSum = 0

  for i in range(N):
    thisX = xs[i]
    thisY = ys[i]

    if thisX <= lX:
      choiceX = rX
      lenX = rXlen
    else:
      choiceX = lX
      lenX = lXlen
    if thisY <= lY:
      choiceY = rY
      lenY = rYlen
    else:
      choiceY = lY
      lenY = lYlen

    dX = thisX - choiceX
    dY = thisY - choiceY

    if dX < 0: dX = -dX
    if dY < 0: dY = -dY

    if maxDSum > dX + dY:
      continue
    else:
      maxDSum = dX + dY
    
    total_len = lenX + lenY - maxDSum

    if answer > total_len:
      answer = total_len
      answer_x = choiceX
      answer_y = choiceY
    elif answer == total_len:
      if answer_x > choiceX:
        answer_x = choiceX
        answer_y = choiceY
      elif answer_x == choiceX:
        if answer_y > choiceY:
          answer_y = choiceY
  
  print(answer)
  print(answer_x, answer_y)

mainF()