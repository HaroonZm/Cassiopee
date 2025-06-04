from itertools import islice, accumulate
from collections import Counter

n, k = map(int, input().split())

first_row = [4, 2, 0, 9, 7]
rows = [first_row]
modulo = 11

# Efficiently generate all 11 needed rows using accumulate and islice
for _ in range(10):
    rows.append([(elem + 8) % modulo for elem in rows[-1]])

flat_counts = [Counter(row)[k] for row in rows]

full_cycles, remainder = divmod(n - 2, modulo)
ans = full_cycles * sum(flat_counts) + sum(islice(flat_counts, remainder))
print(ans)