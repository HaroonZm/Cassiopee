while True:
  n = int(input())
  if n == 0:
    break

  def_dic = {}
  for _ in range(n):
    s, p = input().split()
    def_dic[s] = int(p)
  
  m = int(input())
  com_dic = {}
  for _ in range(m):
    lst = input().split()
    com_dic[lst[0]] = lst[2:]
  
  price_dic = {}
  
  def get_price(t):
    if t in price_dic:
      return price_dic[t]
    if t not in com_dic:
      price_dic[t] = def_dic[t]
      return def_dic[t]
    
    x = 0
    for q in com_dic[t]:
      x += get_price(q)
    ret = min(x, def_dic[t])
    price_dic[t] = ret
    return ret
  
  print(get_price(input()))