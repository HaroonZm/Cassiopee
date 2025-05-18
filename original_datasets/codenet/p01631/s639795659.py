def main():
  n = int(input())
  lst = []
  for _ in range(n):
    word, score = input().split()
    lst.append((word, int(score)))
  mp = ["#" * 6] + ["#" + input() + "#" for _ in range(4)] + ["#" * 6]
  t = int(input())
  
  def search(word):
    used = [[False] * 6 for _ in range(6)]
    vec = ((1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1))
    
    def _search(word, pos, x, y):
      if pos == len(word) - 1:return 1
      used[y][x] = True
      ret = 0
      for dx, dy in vec:
        nx, ny = x + dx, y + dy
        if not used[ny][nx] and mp[ny][nx] == word[pos + 1]:
          ret += _search(word, pos + 1, nx, ny)
      used[y][x] = False
      return ret
    
    ret = 0
    for y in range(1, 5):
      for x in range(1, 5):
        if mp[y][x] == word[0]:ret += _search(word, 0, x, y)  
    return ret
  
  items = []
  for word, score in lst:
    cnt = search(word)
    acc = 1
    weight = len(word)
    while cnt >= acc:
      cnt -= acc
      items.append((score * acc, weight * acc))
      acc *= 2
    if cnt:
      items.append((score * cnt, weight * cnt))
  
  dp = [0] * (t + 1)
  for v, w in items:
    for x in range(t - w, -1, -1):
      if dp[x + w] < dp[x] + v:dp[x + w] = dp[x] + v
  print(max(dp)) 

main()