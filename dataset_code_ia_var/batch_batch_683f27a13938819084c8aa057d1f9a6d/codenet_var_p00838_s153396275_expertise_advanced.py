from functools import lru_cache
from itertools import product

def rotateX(d): return (d[1], d[5], d[2], d[3], d[0], d[4])
def rotateY(d): return (d[3], d[1], d[0], d[5], d[4], d[2])
def rotateZ(d): return (d[0], d[2], d[4], d[1], d[3], d[5])

def all_orientations(dice):
    """Generate all 24 possible orientations of the dice as tuples."""
    seen = set()
    dq = [dice]
    for _ in range(6):  # 6 possible top faces
        nd = dq[-1]
        for _ in range(4):  # rotate around vertical axis
            if nd not in seen:
                seen.add(nd)
                yield nd
            nd = rotateZ(nd)
        if _ % 2 == 0:
            nd = rotateX(nd)
        else:
            nd = rotateY(nd)
        dq.append(nd)

def check(colors, n, s_count):
    diff = [[0]*s_count for _ in range(6)]
    last = colors[-1]
    for dice in colors[:-1]:
        for i in range(6):
            if last[i] != dice[i]:
                diff[i][dice[i]] += 1
    count = 0
    for c in diff:
        c_max, c_sum = max(c), sum(c)
        count += min(c_sum, n-c_max)
    return count

def solve(colors, n, s_count, idx=0, ans=float('inf')):
    if idx == len(colors) - 1:
        return min(ans, check(colors, n, s_count))
    orientation_set = set()
    min_ans = ans
    for orient in all_orientations(tuple(colors[idx])):
        if orient in orientation_set:
            continue
        orientation_set.add(orient)
        original = colors[idx]
        colors[idx] = list(orient)
        min_ans = min(min_ans, solve(colors, n, s_count, idx+1, min_ans))
        colors[idx] = original
    return min_ans

while True:
    try:
        n = int(input())
        if n == 0: break
        memo = {}
        s_count = 0
        color_list = []
        for _ in range(n):
            dice = []
            for s in input().split():
                if s not in memo:
                    memo[s] = s_count
                    s_count += 1
                dice.append(memo[s])
            color_list.append(dice)
        if n == 1:
            print(0)
            continue
        ans = solve(color_list, n, s_count)
        print(ans)
    except EOFError:
        break