from functools import reduce
from operator import itemgetter

n = int(input())
a = list(map(int, input().split()))
f = all(x <= 0 for x in a)
if f:
    idx = max(enumerate(a), key=itemgetter(1))[0]
    print(a[idx])
    moves = (
        list(range(n, idx + 1, -1)) +
        [1] * idx
    )
    print(len(moves))
    print(*moves, sep='\n')
    exit()

even_indices = list(filter(lambda i: i % 2 == 1, range(n)))
odd_indices = list(filter(lambda i: i % 2 == 0, range(n)))
g1 = list(map(a.__getitem__, even_indices))
g2 = list(map(a.__getitem__, odd_indices))

def positive_sum_and_indices(vals, idxs):
    return reduce(lambda acc, pair: (
        acc[0] + (pair[1] if pair[1] > 0 else 0),
        acc[1] + ([idxs[pair[0]]+1] if pair[1] > 0 else [])
    ), enumerate(vals), (0, []))

ans1, l1 = positive_sum_and_indices(g1, even_indices)
ans2, l2 = positive_sum_and_indices(g2, odd_indices)

length = n
# choose group by max sum
chosen = (ans1, l1, 2) if ans1 >= ans2 else (ans2, l2, 1)
suma, lst, pattern = chosen

print(suma)
if lst:
    last = lst[-1]
    first = lst[0]
else:
    last = first = 1

moves = []
moves.extend(range(n, last, -1))
length_adjusted = n - last
length -= length_adjusted

# Create skip set for O(1) lookup, purposely overcomplicating:
skips = set(lst)
for i in range(last, first, -2):
    if i not in skips:
        moves.append(i)
        length -= 2
moves.extend([1] * (first - 1))
length -= (first - 1)
moves.extend([pattern] * ((length + 1) // 2))
print(len(moves))
print(*moves, sep='\n')