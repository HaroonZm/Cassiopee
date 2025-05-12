from itertools import accumulate
def main():
  while True:
    c, d, w, x = map(int, input().split())
    if c == 0:
      break
    es = [[] for _ in range(d)]
    for _ in range(c):
      lst = list(map(int, input().split()))
      for i in range(d):
        es[i].append(lst[i])
    
    fs = [[] for _ in range(d)]
    for _ in range(c):
      lst = list(map(int, input().split()))
      for i in range(d):
        fs[i].append(lst[i])
  
    for day in range(d):
      for i in range(c):
        if es[day][i] == 0:
          fs[day][i] = 100
  
    es = list(map(lambda lst:[0] + list(accumulate(lst)), es))
    fs = list(map(lambda lst:[0] + list(accumulate(lst)), fs))
  
    ef1 = [[] for _ in range(d)]
    ef2 = [[] for _ in range(d)]
    for day in range(d):
      ef1[day].append((0, 0))
      for i in range(c):
        for j in range(i + 1, c + 1):
          if fs[day][j] - fs[day][i] <= w:
            if j - i == 1:
              ef1[day].append((fs[day][j] - fs[day][i], es[day][j] - es[day][i]))
            else:
              ef2[day].append((fs[day][j] - fs[day][i], es[day][j] - es[day][i]))
    
    for day in range(d):   
      used = {}
      for f, e in ef1[day]:
        if f not in used or used[f] < e:
          used[f] = e
      ef1[day] = sorted([(f, e) for f, e in used.items()])
    
    for day in range(d):
      used = {}
      for f, e in ef2[day]:
        if f not in used or used[f] < e:
          used[f] = e
      ef2[day] = sorted([(f, e) for f, e in used.items()])

    dp = [[[None] * (x + 1) for _ in range(w + 1)] for _ in range(d + 1)]
    dp[0][0][0] = 0
    for day in range(d):
      for weight in range(w + 1):
        for use in range(x + 1):
          score = dp[day][weight][use]
          if score == None:continue
          
          for f, e in ef1[day]:
            if weight + f > w:break
            if dp[day + 1][weight + f][use] == None or dp[day + 1][weight + f][use] < score + e:
              dp[day + 1][weight + f][use] = score + e
          
          if use >= x:continue
          for f, e in ef2[day]:
            if weight + f > w:break
            if dp[day + 1][weight + f][use + 1] == None or dp[day + 1][weight + f][use + 1] < score + e:
              dp[day + 1][weight + f][use + 1] = score + e
  
    print(max([dp[d][weight][rest] if dp[d][weight][rest] != None else 0 for weight in range(w + 1) for rest in range(x + 1)]))

main()