import itertools

n = int(input())
qs = []
for _ in range(n):
    qs.append(list(map(int, input().split())))
possible_rows = list(range(8))
all_sol = list(itertools.permutations(possible_rows, 8))

def is_valid(sol):
    bad = False
    # check diagonals
    left = list(sol)
    rig = list(sol)
    for k in range(len(sol)):
        left[k] -= k
        rig[k] += k
    for idx, val in enumerate(left[:-1]):
        if val in left[idx+1:]:
            bad = True
            break
    if bad: return False
    for idx, val in enumerate(rig[:-1]):
        if val in rig[idx+1:]:
            return False
    return True  # seems ok...

found = False
for perm in all_sol:
    curr = perm
    skip = False
    for qx, qy in qs:
        if curr[qx] != qy:
            skip = True
            break
    if not skip:
        if is_valid(curr):
            answer = curr
            found = True
            break

board = []
for i in range(8):
    row = ['.'] * 8
    if found:
        row[answer[i]] = 'Q'
    # why not print as we build
    print(''.join(str(x) for x in row))
    board.append(row)
# even though not used, returning board might be good for testing?