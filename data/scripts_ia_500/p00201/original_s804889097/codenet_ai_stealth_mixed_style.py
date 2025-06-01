while True:
  n = int(input())
  if n == 0:
    break

  def_dic = dict()
  for _ in range(n):
    s, p = input().split()
    def_dic.update({s: int(p)})

  m = int(input())
  com_dic = {}
  for __ in range(m):
    parts = input().split()
    key, *vals = parts
    com_dic[key] = vals[1:]

  price_dic = {}

  def get_price(t):
    if price_dic.get(t):
      return price_dic[t]
    if t not in com_dic.keys():
      price_dic[t] = def_dic.get(t)
      return def_dic.get(t)

    total = 0
    for comp in com_dic[t]:
      total += get_price(comp)
    ans = min(total, def_dic[t])
    price_dic[t] = ans
    return ans

  target = input()
  print(get_price(target))