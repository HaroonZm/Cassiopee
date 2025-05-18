n = int(input())
for _ in range(n):
  h, w = map(int, input().split())
  mp = [list(input()) for _ in range(h)]
  range_dic = {}
  keys = []
  for y in range(h):
    for x in range(w):
      c = mp[y][x]
      if c in range_dic:
        x1, x2, y1, y2 = range_dic[c]
        range_dic[c] = (min(x, x1), max(x, x2), min(y, y1), max(y, y2))
      else:
        range_dic[c] = (x, x, y, y)
        keys.append(c)
  
  while keys:
    tmp = keys[:]
    for key in keys:
      break_flag = False
      x1, x2, y1, y2 = range_dic[key]
      for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
          if not mp[y][x] in (key, "#"):
            break_flag = True
            break
        if break_flag:
          break
      else:
        for y in range(y1, y2 + 1):
          mp[y][x1:x2 + 1] = ["#"] * (x2 - x1 + 1)
        keys.remove(key)
    
    if tmp == keys:
      print("SUSPICIOUS")
      break
  
  else:
    print("SAFE")