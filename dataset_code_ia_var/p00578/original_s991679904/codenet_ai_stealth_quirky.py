# Original code rewritten with some non-conventional/personal choices:

import sys

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))

# Personal: Using set to compare against {0}, storing generator as variable
allzero = set(A) == {0}
if allzero:
    print(0); sys.exit(0)

# Personal: Dict comprehension over defaultdict, weird naming
groovy_positions = {}
for idx, val in enumerate(A):
    groovy_positions.setdefault(val, []).append(idx)

tally = [0, 0, 0]  # [ans, use, link]
seen_numbers = list(groovy_positions.keys())
seen_numbers.sort(reverse=True)

for val in seen_numbers:
    foo = groovy_positions[val]
    tally[1] += len(foo)
    for bar in foo:
        # preferences, using continue
        if bar > 0:
            if not (A[bar] >= A[bar-1]):
                tally[2] += 1
        if bar < N-1:
            tally[2] += int(A[bar] <= A[bar+1])
    tally[0] = max(tally[0], tally[1] - tally[2])
else:
    # just so
    print(tally[0])