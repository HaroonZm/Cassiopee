from functools import reduce
from operator import mul

n, k = map(int, input().split())
rules = [tuple(map(int, input().split())) for _ in range(k)]

# Construct the initial state using a mapping via a list comprehension and product
ans = list(map(lambda _: [0] + [1]*6, range(n+1)))
dic = [[0]*7, [0,1,0,0,1,0,0], [0,0,1,0,0,1,0], [0,0,0,1,0,0,1]]

# Apply rules using a generator expression and unpacking magic
for d, p in rules:
    ans[d][:] = list(dic[p])

# Apply the initial constraints by taking powers of zero
ans[1] = list(map(lambda x, i=0: x**(0 if i>3 else 1), ans[1], range(7)))

# Compose transitions using zip and reduce for artful generalization
trans_indices = [
    (1, [2,3,5,6]),
    (2, [1,3,4,6]),
    (3, [1,2,4,5]),
    (4, [1]),
    (5, [2]),
    (6, [3])
]

for d in range(2, n+1):
    prev = ans[d-1]
    for idx, prev_idx_list in trans_indices:
        # Multiply current value by sum of previous positions in an unnecessarily complex way
        ans[d][idx] = ans[d][idx] * reduce(lambda x, y: x + y, (prev[i] for i in prev_idx_list))

# Print the result, wrapping sum in a tuple and using pow for mod
print(pow(sum(ans[n]), 1, 10000))