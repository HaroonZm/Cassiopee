import sys
input = sys.stdin.readline
while True:
  n, m, k, l = map(int, input().split())
  if n == 0:
    break
  ranking = []
  for _ in range(n):
    name, x = input().split()
    x = int(x)
    ranking.append([x, name])
  ranking.sort(key=lambda x:(-x[0], x[1]))
  
  favs = {input().strip() for _ in range(m)}
  favs_x = {}
  not_favs_x = {}
  for x, name in ranking:
    if name in favs:
      favs_x[name] = x
    else:
      not_favs_x[name] = x
  favs_ranking = sorted(favs_x.items(), key=lambda x:(-x[1], x[0]))
  not_favs_ranking = sorted(not_favs_x.items(), key=lambda x:(-x[1], x[0]))
  not_favs_length = len(not_favs_ranking)
  favs_length = len(favs_ranking)
  def check(num):
    not_favs_num = k - num
    if num > favs_length:
      return False
    if not_favs_num >= not_favs_length:
      return True
    target_name, target_x = not_favs_ranking[not_favs_num]
    need = 0
    for name, x in favs_ranking[:num]:
      if target_name > name:
        if target_x <= x:
          continue
        else:
          need += target_x - x
  
      else:
        if target_x < x:
          continue
        else:
          need += target_x - x + 1
    
    return (need <= l)
  
  left = 0
  right = min(k, favs_length) + 1

  while True:
    if right <= left + 1:
      break
    center = (left + right) // 2
    if check(center):
      left = center
    else:
      right = center
  print(left)