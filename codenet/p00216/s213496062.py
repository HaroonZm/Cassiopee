def fee(w):
  acc = 1150
  if w <= 10:
    return acc
  w -= 10
  if w <= 10:
    return acc + 125 * w
  acc += 1250
  w -= 10
  if w <= 10:
    return acc + 140 * w
  acc += 1400
  w-= 10
  return acc + 160 * w

while True:
  w = int(input())
  if w == -1:
    break
  print(4280 - fee(w))