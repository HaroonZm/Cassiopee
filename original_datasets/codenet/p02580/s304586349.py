from collections import defaultdict as dd
def solve():
  h, w, m = map(int, input().split())
  
  targets = set()
  rows = dd(int)
  cols = dd(int)
  for _ in range(m):
    r, c = map(int, input().split())
    rows[r] += 1
    cols[c] += 1
    targets.add((r, c))
    
  best_rows = []
  best_cols = []
  best_row = max(rows.values())
  best_col = max(cols.values())
  best = best_row + best_col - 1
  for k, v in rows.items():
    if v == best_row:
      best_rows.append(k)
  for k, v in cols.items():
    if v == best_col:
      best_cols.append(k)
  
  for row in best_rows:
    for col in best_cols:
      if (row, col) not in targets:
        print (best + 1)
        return
  print (best)
solve()