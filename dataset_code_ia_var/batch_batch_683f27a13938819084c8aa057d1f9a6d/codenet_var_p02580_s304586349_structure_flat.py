from collections import defaultdict as dd

h, w, m = map(int, input().split())

targets = set()
rows = dd(int)
cols = dd(int)

for _ in range(m):
    r, c = map(int, input().split())
    rows[r] += 1
    cols[c] += 1
    targets.add((r, c))

best_row = 0
for v in rows.values():
    if v > best_row:
        best_row = v

best_col = 0
for v in cols.values():
    if v > best_col:
        best_col = v

best_rows = []
for k, v in rows.items():
    if v == best_row:
        best_rows.append(k)

best_cols = []
for k, v in cols.items():
    if v == best_col:
        best_cols.append(k)

found = False
for row in best_rows:
    for col in best_cols:
        if (row, col) not in targets:
            print(best_row + best_col)
            found = True
            break
    if found:
        break

if not found:
    print(best_row + best_col - 1)