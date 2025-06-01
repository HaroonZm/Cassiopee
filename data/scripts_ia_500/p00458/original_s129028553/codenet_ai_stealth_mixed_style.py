def solve():
  while True:
    m, n = int(input()), int(input())
    if m == 0:
      break
    ices = []
    for _ in range(n):
      row = list(map(int, input().split()))
      ices.append([0] + row + [0])
    ices.insert(0, [0] * (m + 2))
    ices.append([0] * (m + 2))

    score = []
    for _ in range(n+2):
      score.append([0]*(m+2))

    for x in range(1, n+1):
      for y in range(1, m+1):
        if ices[x][y] != 0:
          score[x-1][y] += 1
          score[x+1][y] += 1
          score[x][y-1] += 1
          score[x][y+1] += 1

    def bfs(x, y, imap, acc):
      imap[x][y] = 0
      acc += 1
      out = [acc]
      if imap[x-1][y]:
        out.append(bfs(x-1, y, imap, acc))
      if imap[x+1][y]:
        out.append(bfs(x+1, y, imap, acc))
      if imap[x][y-1]:
        out.append(bfs(x, y-1, imap, acc))
      if imap[x][y+1]:
        out.append(bfs(x, y+1, imap, acc))
      imap[x][y] = 1
      return max(out)

    max_ans = 0
    for r in range(1, n+1):
      for c in range(1, m+1):
        if score[r][c] in (1, 2) and ices[r][c]:
          tmp = bfs(r, c, ices, 0)
          if tmp > max_ans:
            max_ans = tmp

    print(max_ans)

solve()