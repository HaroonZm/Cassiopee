from functools import reduce
from operator import add, sub

n = int(input())
m = int(input())

deltas = [tuple(map(int, input().split())) for _ in range(n)]

traj = [m] + list(
    reduce(
        lambda acc, ab: acc + [acc[-1] + ab[0] - ab[1] if acc[-1] >= 0 else acc[-1]],
        deltas,
        [m]
    )[1:]
)

filtered_traj = list(map(lambda x: x if x >= 0 else 0, traj))
print(max(filtered_traj))