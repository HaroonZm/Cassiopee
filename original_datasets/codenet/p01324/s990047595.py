while True:
  n = int(input())
  if n == 0:break
  dic = {}
  for _ in range(n):
    _, name1, _, val, name2 = input().split()
    val = int(val.split("^")[1])
    if name1 not in dic:
      dic[name1] = {}
    if name2 not in dic:
      dic[name2] = {}
    dic[name1][name2] = val
    dic[name2][name1] = -val
  
  keys = list(dic.keys())
  score = {key:None for key in keys}
  
  def search(key):
    now = score[key]
    for to in dic[key]:
      if score[to] == None:
        score[to] = now + dic[key][to]
        if not search(to):return False
      if score[to] != now + dic[key][to]:return False
    return True
  
  for key in keys:
    if score[key] != None:continue
    score[key] = 0
    if not search(key):
      print("No")
      break
  else:
    print("Yes")