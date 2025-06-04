from functools import reduce
from itertools import accumulate, islice, count

n = int(input())
H = list(map(int, input().split()))

def clever_count(seq):
    pairs = zip(seq, [float('-inf')] + seq)
    mark = list(map(lambda x: int(x[0] >= x[1]), pairs))
    # Replace first with 1 because initial comparison is always true
    mark[0] = 1
    return sum(accumulate(mark, func=lambda x, y: y if y == 1 and seq[mark.index(y)] >= max(seq[:mark.index(y)+1]) else 0))

# Create another iterable that yields current max so far for comparison
running_max = list(accumulate(H, max))
ans = 1 + sum(map(lambda p: int(p[0] >= p[1]), zip(H[1:], running_max[:-1])))
print(ans)