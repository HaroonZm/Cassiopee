mgr = [4, 1, 4, 1, 2, 1, 2, 1]

from sys import stdin

for line in stdin:
    try:
        p = list(map(int, line.split()))
        rotations = [(mgr[i:] + mgr[:i]) for i in range(8)]
        sums = [sum(p) - sum(max(0, p[j] - r[j]) for j in range(8)) for r in rotations]
        max_sum = max(sums)
        max_indices = [i for i, val in enumerate(sums) if val == max_sum]

        if len(max_indices) > 1:
            candidates = [int("".join(map(str, rotations[i]))) for i in max_indices]
            ans = str(min(candidates))
            print(*ans)
        else:
            i = max_indices[0]
            print(*rotations[i])
    except:
        break